from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    satellite_products: list = [
            'CHIRSP (Rainfall Estimates from Rain Gauge and Satellite Observations)',
            'EAR5',
            'MODIS NDVI/EVI (16-Days)',
            'MODIS Land Surface Temperature',
            'MODIS Vegetation/Water Index',
            'SRTM Elevation'
        ]
    product_type: list = [
            'Zonal Statistic (csv structured data)',
            'Raster(tiff structured data)'
        ]
    message: str = 'Must choose at least one'

    chrisp_bands_list: list = ['precipitation']
    era5_bands_list: list = ['Air_2m_T_C_mean', 'Air_2m_T_C_min', 'Air_2m_T_C_max', 'dewpoint_2m_C', 'RH', 'mean_2m_air_temperature', 'minimum_2m_air_temperature',
                            'maximum_2m_air_temperature','dewpoint_2m_temperature','total_precipitation','surface_pressure','mean_sea_level_pressure', 
                            'u_component_of_wind_10m', 'v_component_of_wind_10m']
    modis_ndvi_evi_bands_list: list = ['NDVI', 'EVI']
    modis_lst_bands_list: list = ['LST_Day','LST_Night','LST_Mean']
    modis_nadir_bands_list: list = ['NDVI','EVI','SAVI','NDWI_Gao', 'NDWI_Mc', 'MNDWI']

