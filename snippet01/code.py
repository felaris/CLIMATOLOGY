import pandas
import netCDF4 as nc
import numpy as np
import csv
import glob
import sys
from pathlib import Path

filename = Path(
    '_grib2netcdf-webmars-public-svc-green-005-6fe5cac1a363ec1525f54343b6cc9fd8-XM_YF6.nc')
# def to_csv(source_file):
# nc data
dataset = nc.Dataset(filename)
print(dataset.variables.keys())

# Get the corresponding array collection - latitude longitude temperature depth
lat = dataset.variables['latitude'][:]
lon = dataset.variables['longitude'][:]
press = dataset.variables['sp'][:]
eva = dataset.variables['e'][:]

Index = []  # put the latitude and longitude of the condition into the list index
for j in range(len(lat)):  # j is latitude

    for k in range(len(lon)):  # k is longitude
        if lat[j] > 2 and lat[j] < 112:
            if lon[k] > 1 and lon[k] < 315:
                # Insert data that satisfies the condition
                Index.append((j, k))

    # print('-------------------------------------------------------------------')
         #  does not contain an extension
filename = filename.split('.')
file_name = filename[0]

# Create csv object file
try:
    # Open target csv file
    with open(file_name+'.csv', 'a', newline='') as targetFile:
        # Create a write stream
        writer = csv.writer(targetFile)
        # Write header
        writer.writerow(('lat', 'lon', 'pressure',  'evaporation',
                         ))
        # data input
    for j in range(len(lat)):  # j is latitude
        for k in range(len(lon)):  # k is longitude
            if lat[j] > 2 and lat[j] < 112:
                if lon[k] > 1 and lon[k] < 315:
                    i = 0
                    writer.writerow(
                        (lat[j], lon[k], press[0][i][j][k],  eva[i]))

#  # Close the file

#print('Get'+file_name+'.csv Success!')

targetFile.close()