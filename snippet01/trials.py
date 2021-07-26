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


filename = Path('pressure_evaporation_with_time_and_lon_lat.nc')

data = xr.open_dataset(filename)
print(data)
press = data['sp']
eva = data['e']

print(eva)

df_press = press.sel(longitude = np.arange(-25,50,0.5), latitude = np.arange(0,40,0.5), method='nearest')

df_press[1].plot()