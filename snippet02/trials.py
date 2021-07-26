#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:44:17 2021

@author: felaris
"""

# Importing libraries
import pandas as pd
import netCDF4 as nc
import numpy as np
import csv
import glob
import sys
from pathlib import Path
import pymannkendall as pmk
import xarray as xr
import matplotlib.pyplot as plt 


filename = Path('pressure_evaporation_with_time_and_lon_lat.nc')

data = xr.open_dataset(filename)
print(data)
press = data['sp']
eva = data['e']


#Northern hemeisphere graphs 
NHA_press = press.sel(longitude = np.arange(-25,50,0.5), latitude = np.arange(0,40,0.5), method='nearest')
NHA_eva = eva.sel(longitude = np.arange(-25,50,0.5), latitude = np.arange(0,40,0.5), method='nearest')

'''
# Doing same for Evaporation 
df_eva[0].plot()
plt.savefig('evaporation.jpeg')

#Plotting different kinds of graphs for pressure 
df_press[0,1,1].plot()
plt.savefig('pressure.jpeg')'''


NHA_press.groupby('time.month').mean(dim=('time','longitude')).T.plot()





