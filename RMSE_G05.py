# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:48:05 2024

@author: User
"""

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from sklearn.metrics import mean_squared_error

# Function to read data from NetCDF file
def ncread(file_name, vname):
    fil = netCDF4.Dataset(file_name, 'r')
    dat = np.asarray(fil.variables[vname][:])
    fil.close()
    return dat

# Function to clip image based on given boundary
def clip_image(lat, lon, lat_b, lon_b):
    min_lat_b = np.abs(lat - lat_b[1]).argmin()
    max_lat_b = np.abs(lat - lat_b[0]).argmin()
    min_lon_b = np.abs(lon - lon_b[0]).argmin()
    max_lon_b = np.abs(lon - lon_b[1]).argmin()
    return min_lat_b, max_lat_b, min_lon_b, max_lon_b

# Function to read data within the given boundary
def read_example_data_tem(file_name, boundary):
    data = ncread(file_name, 'temp2m')
    lat = ncread(file_name, 'lat')
    lon = ncread(file_name, 'lon')
    clat1, clat2, clon1, clon2 = clip_image(lat, lon, (boundary[0], boundary[1]), (boundary[2], boundary[3]))
    lat = lat[clat1:clat2+1]
    lon = lon[clon1:clon2+1]
    data = data[clat1:clat2+1, clon1:clon2+1]
    return data, lat, lon

# Function to read data within the given boundary
def read_example_data_wind(file_name, boundary):
    data = ncread(file_name, 'wind10m')
    lat = ncread(file_name, 'lat')
    lon = ncread(file_name, 'lon')
    clat1, clat2, clon1, clon2 = clip_image(lat, lon, (boundary[0], boundary[1]), (boundary[2], boundary[3]))
    lat = lat[clat1:clat2+1]
    lon = lon[clon1:clon2+1]
    data = data[clat1:clat2+1, clon1:clon2+1]
    return data, lat, lon

################################################################
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
boundary = (8, 16, 100, 112)  # Define boundary here
RMSE= np.zeros(len(months))
for i in range(len(months)):
    file_name_forecast = "temp2m_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    file_name_analysis = "temp2m_r_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    data_forecast, lat, lon = read_example_data_tem(file_name_forecast, boundary)  # Call read_example_data inside the loop
    data_analysis, lat, lon = read_example_data_tem(file_name_analysis, boundary)  # Call read_example_data inside the loop
    mse = mean_squared_error(data_analysis, data_forecast)
    RMSE[i] = np.sqrt(mse)    
print("Root Mean Squared Error (RMSE):", RMSE)

# Make Bar plot
barWidth = 0.25
plt.figure(figsize=(8,4))
plt.bar(months, RMSE, color='teal', width = barWidth, label = '2023')
plt.title('RMSE Temperature ')
plt.xlabel('Months')
plt.ylabel('2m Temperature (k)')
plt.legend()
plt.show()


for i in range(len(months)):
    file_name_forecast = "wind10m_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    file_name_analysis = "wind10m_r_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    data_forecast, lat, lon = read_example_data_wind(file_name_forecast, boundary)  # Call read_example_data inside the loop
    data_analysis, lat, lon = read_example_data_wind(file_name_analysis, boundary)  # Call read_example_data inside the loop
    mse = mean_squared_error(data_analysis, data_forecast)
    RMSE[i] = np.sqrt(mse)    
print("Root Mean Squared Error (RMSE):", RMSE)

# Make Bar plot
barWidth = 0.25
plt.figure(figsize=(8,4))
plt.bar(months, RMSE, color='purple', width = barWidth, label = '2023')
plt.title('RMSE Wind ')
plt.xlabel('Months')
plt.ylabel('10 m Wind (ms-1)')
plt.legend()
plt.show()