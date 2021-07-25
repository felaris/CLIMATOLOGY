import pandas
import netCDF4 as ne
import numpy as np
import  csv
import glob
import  sys
 
def to_csv(source_file):
    # nc data
    dataset=ne.Dataset(source_file)
    print(dataset.variables.keys())
 
         #Get the corresponding array collection - latitude longitude temperature depth
    lat_set = dataset.variables['lat'][:]
    lon_set = dataset.variables['lon'][:]
    temp_set=dataset.variables['water_temp'] [:]
    dep_set=dataset.variables['depth'][:]
 
         Index = [] # put the latitude and longitude of the condition into the list index
         For j in range(len(lat_set)): # j is latitude
                 For k in range(len(lon_set)): # k is longitude
            if lat_set[j] > 23 and lat_set[j] < 40:
                if lon_set[k] > 118 and lon_set[k] < 131:
                                         Index.append((j, k)) # Insert data that satisfies the condition
         Print('output index list:')
    print(index)
    print('-------------------------------------------------------------------')
         #  does not contain an extension
    source_file=source_file.split('.')
    file_name=source_file[0]
 
         #Create csv object file
    try:
                 #Open target csv file
        with open(file_name+'.csv','a',newline='') as targetFile:
                         #Create a write stream
            writer = csv.writer(targetFile)
                         #Write header
            writer.writerow(('lat', 'lon', 'temperature',  'depth',
                             ))
                         # data input 
                         For j in range(len(lat_set)): # j is latitude
                                 For k in range(len(lon_set)): # k is longitude
                    if lat_set[j] > 23 and lat_set[j] < 40:
                        if lon_set[k] > 118 and lon_set[k] < 131:
                            i=0
                            writer.writerow((lat_set[j], lon_set[k], temp_set[0][i][j][k],  dep_set[i]))
 
                 targetFile.close()#Close the file
        print('Get'+file_name+'.csv Success!')
         Except Exception as e:# throw an exception
        print('Error :'+str(e))
 
 
if '__name__ ==__main__':
    print("start transfrom!")
    to_csv('20150101.nc')
    print('Transform successfully')