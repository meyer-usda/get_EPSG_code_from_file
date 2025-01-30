### Python script to get EPSG code from a raster or las/laz file

Provide a raster file or a las/laz file and this script will try to pull the EPSG code from the EXIF/header

#### Use these commands to install and run the script:

##### Load packages using conda
- conda create -n getEPSG -c conda-forge python laspy pyproj rasterio
- conda activate getEPSG
- cd ./path/to/the/python/script
##### Commands to run the script (or get help)
- python ./get_EPSG_code_from_file.py --help
- python ./get_EPSG_code_from_file.py -f full/path/to/target/file
