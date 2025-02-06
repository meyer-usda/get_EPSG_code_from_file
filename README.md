### Python script to get EPSG code from a raster or las/laz file

Provide a raster file or a las/laz file and this script will try to pull the EPSG code from the EXIF/header
This was written quickly - reach out to meyer.taffel@usda.gov to troubleshoot

#### Installation and Running Instructions

Open anaconda powershell/command prompt

##### Load packages using conda (or activate an environment that has these packages installed)
- conda create -n getEPSG -c conda-forge python laspy pyproj rasterio
- conda activate getEPSG
- cd ./path/to/the/python/script
##### Commands to run the script (or get help)
- python ./get_EPSG_code_from_file.py --help
- python ./get_EPSG_code_from_file.py -f full/path/to/target/file
