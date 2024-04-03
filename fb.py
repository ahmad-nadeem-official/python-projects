#####################################################################################
import netCDF4 as nc
import numpy as np
import xarray as xr
from sklearn.model_selection import train_test_split
import xgboost as xgb
# Load historical climate data
rains_obs = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/rains_obs.nc')['pr'][:]
tmax_obs = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/tmax_obs.nc')['tasmax'][:]
tmin_obs = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/tmin_obs.nc')['tasmin'][:]
# Load past yield data
yield_data = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/MME_data/averaged_yield_final/maize_yield.nc')['var'][:]
yield_time_data = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/MME_data/averaged_yield_final/maize_yield.nc')['time'][:]
lon_data = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/MME_data/averaged_yield_final/maize_yield.nc')['lon'][:]
lat_data = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/MME_data/averaged_yield_final/maize_yield.nc')['lat'][:]

# Convert to DataArrays for manipulation
rains_da = xr.DataArray(rains_obs)
tmax_da = xr.DataArray(tmax_obs)
tmin_da = xr.DataArray(tmin_obs)
yield_da = xr.DataArray(yield_data)

# Reshape climate data into a 2D array (
climate_data = np.column_stack((rains_da.values.flatten(), tmax_da.values.flatten()))
#climate_data = np.column_stack((rains_da.values.flatten(), tmax_da.values.flatten(), tmin_da.values.flatten()))
# Flatten yield data to match the climate data
reshaped_yield = yield_da.values.flatten()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(climate_data, reshaped_yield, test_size=0.2, random_state=42)
nan_indices = np.isnan(y_train)
if np.any(nan_indices):
  # Replace NaN values with 0
  y_train[nan_indices] = 0.0
# Initialize and train the XGBoost regression model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Load future climate projection data
p_rains = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/P_rains.nc')['pr'][:]
p_tmax = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/P_tmax.nc')['tasmax'][:]
p_tmin = nc.Dataset('/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/P_tmin.nc')['tasmin'][:]

dataset = xr.open_dataset("/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/P_tmax.nc")
#time_values = dataset.variables['time']
#time_data = time_values.values

# Prepare the future climate data for prediction (similar preprocessing as historical data)
future_climate_data = np.column_stack((p_rains.data.flatten(), p_tmax.data.flatten()))

# Use the trained model to predict future yield
predicted_yield = model.predict(future_climate_data)
# Create a new NetCDF file to store the predicted yields
output_nc_path = '/proj/Luciana/CMIP6_data/Rainfall/pr_models/ssp585_corrected/XG_boost_MODEL/Current_climate_variables_suitability/Predicted_yield/P_maize.nc'
with nc.Dataset(output_nc_path, 'w', format='NETCDF4') as nc_output:
  # Create dimensions
  #nc_output.createDimension('time', len(time_data))
  nc_output.createDimension('lat', len(lat_data))
nc_output.createDimension('lon', len(lon_data))

# Create variables
#time_var = nc_output.createVariable('time', 'f8', ('time',))
lat_var = nc_output.createVariable('lat', 'f8', ('lat',))
lon_var = nc_output.createVariable('lon', 'f8', ('lon',))
predicted_yield_var = nc_output.createVariable('predicted_yield', 'f8', ('lat', 'lon'))

# Write data to variables
#time_var[:] = time_data
lat_var[:] = lat_data
lon_var[:] = lon_data
predicted_yield_var[:] = predicted_yield.reshape((len(lat_data), len(lon_data)))
#predicted_yield_var[:] = predicted_yield.reshape((len(time_data), len(lat_data), len(lon_data)))

print('Predicted yields saved to:', output_nc_path)