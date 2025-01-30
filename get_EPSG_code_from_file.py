import rasterio, laspy, argparse, os

parser = argparse.ArgumentParser(description='Provide a las file and get the EPSG code from the header')
parser.add_argument('-f', '--file', type=str, help=r'full\path\to\las\file')
args = parser.parse_args()

if args.file:
    filepath = args.file
else:
    # Provide a manual filepath here if you don't put one in the command line
    filepath = r'C:\Users\MeirTaffel\Desktop\G-LiHT_coregister\lidar\AK_20220726_FHP_4_l0s0.las'

filetype = os.path.splitext(filepath)[1]

if filetype in [".las", '.laz']:
    las = laspy.read(filepath)
    epsg = las.header.parse_crs()
else:
    with rasterio.open(filepath) as src:
        epsg = src.crs

print(epsg)