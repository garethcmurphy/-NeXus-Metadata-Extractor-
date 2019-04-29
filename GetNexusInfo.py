#!/usr/bin/env python3
import copy
import h5py
import inspect
import json
import socket
from V20Filenames import V20Filenames


class GetNexusInfo:
    nexusInfo = {}
    filename = "v20.h5"
    metadata = {}
    sfdict = {}
    units = {
        "speed": "Hz",
        "phase": "deg"
    }
    basename = "/users/detector/experiments/"
    sourceFolderArray = V20Filenames.sourceFolderArray

    inv_map = {v: k for k, v in sourceFolderArray.items()}

    def __init__(self):
        self.filename = "v20.h5"

    def get_h5_info(self, key):

        self.nexusInfo = {}

        filename = self.basename + self.sfdict[key]
        print(filename)
        if '.hdf' in filename:
            if '000155.hdf' in filename:
                return
            elif '000156.hdf' in filename:
                return
        elif '.nxs' in filename:
            pass
        else:
            return

        with h5py.File(filename, 'r',  libver='latest', swmr=True) as f:
            self.nexusInfo["creator"] = self.get_attribute(f.attrs, "creator")
            self.nexusInfo["file_name"] = self.get_attribute(
                f.attrs, "file_name")
            self.nexusInfo["file_time"] = self.get_attribute(
                f.attrs, "file_time")
            title = self.get_property(f, "/entry/title")
            self.nexusInfo["title"] = title
            source_name = self.get_property(f, "/entry/instrument/source/name")
            self.nexusInfo["start_time"] = self.get_property(
                f, "/entry/start_time")
            # self.nexusInfo["chopperSpeed"]
            for chopper_number in range(1, 9):
                self.getVar(f, "speed", chopper_number)
            for chopper_number in range(1, 9):
                self.getVar(f, "speed", chopper_number)
            for chopper_number in range(1, 8):
                self.getVar(f, "phase", chopper_number)
            sample_description = self.get_ellipsis(
                f, "/entry/sample/description")
            self.nexusInfo["sample_description"] = sample_description[()]
            self.nexusInfo["source_name"] = source_name
            f.close()
        print(self.nexusInfo)
        self.nexusInfo["file_name"] = filename
        self.metadata[key] = self.nexusInfo

    def getVar(self, f, measurement, number):
        num = str(number)
        array = self.get_property(
            f, "/entry/instrument/chopper_"+num+"/"+measurement)
        value = array
        if hasattr(array, "__iter__"):
            value = array[0]
        self.nexusInfo["chopper_"+measurement+"_" +
                       num] = {"v": str(value), "u": self.units[measurement]}

    def get_names(self, my_list, f, tag):
        if tag in f:
            names = f[tag+"/name"]
            my_list.extend(names)

    def get_attribute(self, attrs, attr):
        value = ""
        if (attr in attrs.keys()):
            value = attrs[attr]
        return value

    def get_property(self, f, path):
        title2 = ""
        if (path in f):
            title = f[path][...]
            title2 = title[()]
        # print(path, title2)
        return title2

    def get_ellipsis(self, f, path):
        if (path in f):
            dset = f[path]
        return dset[...]

    def loop(self):
        hostname = socket.gethostname()
        self.sfdict = self.sourceFolderArray
        if hostname == 'CI0020036':
            self.sfdict = {
                "0001": "nicos_00000108.hdf"
            }
            self.basename = "./"
        for key in self.sfdict:
            self.get_h5_info(key)


if __name__ == "__main__":
    h5 = GetNexusInfo()
    h5.loop()

    print(json.dumps(h5.metadata, indent=2, sort_keys=True))

    filename = "metadata.json"
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(h5.metadata, f, indent=2, sort_keys=True)
