# NeXus Metadata Extractor 📊  

A Python script to extract metadata from NeXus files (HDF5 format) containing neutron experiment data. This tool is designed to simplify the process of retrieving and analyzing metadata for scientific datasets.

---

## Features ✨  

- Extract metadata from NeXus files efficiently.  
- Supports HDF5 file format for neutron data.  
- Outputs metadata in an easily readable format (e.g., JSON, CSV).  

---

## Getting Started 🚀  

### Prerequisites 🛠️  

- Python 3.8+  
- Required Python libraries:
  - `h5py`
  - `pandas`  

Install dependencies:  
pip install h5py pandas  

---

### Installation  

1. Clone the repository:  
git clone https://github.com/your-username/nexus-metadata-extractor.git  
cd nexus-metadata-extractor  

2. Make the script executable:  
chmod +x extract_metadata.py  

---

## Usage 🔧  

### Extract Metadata from a NeXus File  
Run the script with a NeXus file as input:  
python extract_metadata.py path/to/your/nexus_file.nxs  

### Output Options  
- The script outputs metadata in JSON format by default.  
- Add `--csv` to export the metadata as a CSV file:  
  python extract_metadata.py path/to/your/nexus_file.nxs --csv  

---

## File Structure 📂  

- `extract_metadata.py`: The main Python script for metadata extraction.  
- `README.md`: Documentation for the repository.  

---

## Contributing 🤝  

1. Fork the repository.  
2. Create a new branch:  
git checkout -b feature/your-feature  

3. Commit your changes:  
git commit -m "Add your feature"  

4. Push the branch:  
git push origin feature/your-feature  

5. Open a pull request.  

---

## License 📝  

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Easily extract and analyze metadata from NeXus files!** 📊✨  
