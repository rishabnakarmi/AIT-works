# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:38:36 2024

@author: User
"""
import numpy as np
import netCDF4
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

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

fig, axs = plt.subplots(len(months), 1, figsize=(15, 25), subplot_kw={'projection': ccrs.PlateCarree()})

boundary = (8, 16, 100, 112)  # Define boundary here

for i, ax in enumerate(axs):
    file_name = "temp2m_r_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    data, lat, lon = read_example_data_tem(file_name, boundary)  # Call read_example_data inside the loop
    data_p = data[:, :]  # Adjusted to use the i-th month's data
    img = ax.imshow(data_p, cmap='jet', vmin=np.nanmin(data_p), vmax=np.nanmax(data_p), extent=[lon.min(), lon.max(), lat.min(), lat.max()])
    ax.set_title('Temperature ({0} 24)'.format(months[i]))
    ax.coastlines(resolution='10m', color='black')
    ax.gridlines(draw_labels=False)
    
    ax.grid()

# Add a single colorbar
cbar = fig.colorbar(img, ax=axs, orientation='horizontal', fraction=0.011, pad=0.05)
cbar.set_label('Temperature (K)')

plt.show()

################################################################################


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

fig, axs = plt.subplots(len(months), 1, figsize=(15, 25), subplot_kw={'projection': ccrs.PlateCarree()})

boundary = (8, 16, 100, 112)  # Define boundary here

for i, ax in enumerate(axs):
    file_name = "wind10m_r_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    data, lat, lon = read_example_data_wind(file_name, boundary)  # Call read_example_data inside the loop
    data_p = data[:, :]  # Adjusted to use the i-th month's data
    img = ax.imshow(data_p, cmap='RdYlGn', vmin=np.nanmin(data_p), vmax=np.nanmax(data_p), extent=[lon.min(), lon.max(), lat.min(), lat.max()])
    ax.set_title('Wind Speed ({0} 24)'.format(months[i]))
    ax.coastlines(resolution='10m', color='black')
    ax.gridlines(draw_labels=False)
    
    ax.grid()

# Add a single colorbar
cbar = fig.colorbar(img, ax=axs, orientation='horizontal', fraction=0.011, pad=0.05)
cbar.set_label('Wind Speed (m/s)')

plt.show()
#################################################

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

fig, axs = plt.subplots(len(months), 1, figsize=(15, 25), subplot_kw={'projection': ccrs.PlateCarree()})

boundary = (8, 16, 100, 112)  # Define boundary here

for i, ax in enumerate(axs):
    file_name = "wind10m_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    data, lat, lon = read_example_data_wind(file_name, boundary)  # Call read_example_data inside the loop
    data_p = data[:, :]  # Adjusted to use the i-th month's data
    img = ax.imshow(data_p, cmap='RdYlGn', vmin=np.nanmin(data_p), vmax=np.nanmax(data_p), extent=[lon.min(), lon.max(), lat.min(), lat.max()])
    ax.set_title('Wind Speed ({0} 24)'.format(months[i]))
    ax.coastlines(resolution='10m', color='black')
    ax.gridlines(draw_labels=False)
    
    ax.grid()

# Add a single colorbar
cbar = fig.colorbar(img, ax=axs, orientation='horizontal', fraction=0.011, pad=0.05)
cbar.set_label('Wind Speed (m/s)')

plt.show()


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

fig, axs = plt.subplots(len(months), 1, figsize=(15, 25), subplot_kw={'projection': ccrs.PlateCarree()})

boundary = (8, 16, 100, 112)  # Define boundary here

for i, ax in enumerate(axs):
    file_name = "temp2m_2023-{0:02d}.nc".format(i + 1)  # Adjust file name dynamically
    data, lat, lon = read_example_data_tem(file_name, boundary)  # Call read_example_data inside the loop
    data_p = data[:, :]  # Adjusted to use the i-th month's data
    img = ax.imshow(data_p, cmap='jet', vmin=np.nanmin(data_p), vmax=np.nanmax(data_p), extent=[lon.min(), lon.max(), lat.min(), lat.max()])
    ax.set_title('Temperature ({0} 24)'.format(months[i]))
    ax.coastlines(resolution='10m', color='black')
    ax.gridlines(draw_labels=False)
    
    ax.grid()

# Add a single colorbar
cbar = fig.colorbar(img, ax=axs, orientation='horizontal', fraction=0.011, pad=0.05)
cbar.set_label('Temperature (K)')

plt.show()