import rasterio, laspy, argparse, os

parser = argparse.ArgumentParser(description='Provide a raster or las/laz file and get the EPSG code from the EXIF/header')
parser.add_argument('-f', '--file', type=str, help=r'full\path\to\target\file')
args = parser.parse_args()

if args.file:
    filepath = args.file
else:
    # Provide a manual filepath here if you don't put one in the command line
    filepath = r'C:\Users\MeirTaffel\Desktop\G-LiHT_coregister\lidar\AK_20220726_FHP_4_l0s0.las'

filetype = os.path.splitext(filepath)[1]

if filetype in [".las", '.laz']:
    try:
        las = laspy.read(filepath)
        print(las.header.parse_crs())
    except:
        print("Couldn't find the EPSG code in your file header.")
else:
    try:
        with rasterio.open(filepath) as src:
            print(src.crs)
    except:
        print("Couldn't find EPSG code. Check if your file type is a raster format (.tif, etc)")
