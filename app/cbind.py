from flask import session
from setting.config import settings
import pandas as pd
import glob
import os


def _rename_columns(df, column_name, suffix):
    if column_name in df.columns:
        df.rename(columns={column_name: f"{column_name}_{suffix}"}, inplace=True)

def cbind_chirsp(statics, files_folder):

    all_files = glob.glob(os.path.join(files_folder, "Prec_{}*.csv".format(statics)))
    
    df_from_each_file = (pd.read_csv(f, sep = ",") for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index = True)
    if 'precipitation' in df_merged.columns.tolist():
        df_merged.rename(columns={'precipitation' : 'precipitation_' + str(statics)}, inplace = True)
    else:
        pass

    df_merged.to_csv(files_folder + '/final.csv', index=False)


def cbind_era5(statics):
    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])

    all_files = glob.glob(os.path.join(user_folder, "Era5_{}*.csv".format(statics)))
    
    df_from_each_file = (pd.read_csv(f, sep = ",") for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index = True)

    for column_name in df_merged.columns:
        if column_name in settings.era5_bands_list:
            _rename_columns(df_merged, column_name, str(statics))

    df_merged.to_csv(user_folder + '/final.csv', index=False)
    

def cbind_Modis_NDVI_EVI(statics):

    all_files = glob.glob(os.path.join(session['uder_id'],"Modis_NDVI_EVI_{}*.csv".format(statics)))

    df_from_each_file = (pd.read_csv(f, sep = ",") for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    if 'NDVI' in df_merged.columns.tolist():
        df_merged.rename(columns={'NDVI' : 'NDVI_' + str(statics)}, inplace=True)
    else:
        pass
    if 'EVI' in df_merged.columns.tolist():
        df_merged.rename(columns={'EVI' : 'EVI_' + str(statics)}, inplace=True)
    else:
        pass
    
    df_merged.to_csv(session['user_id'] + '/final.csv',index=False)


def cbind_Modis_LST(statics):

    all_files = glob.glob(os.path.join(session['user_id'],"Modis_LST_{}*.csv".format(statics)))

    df_from_each_file = (pd.read_csv(f, sep = ",") for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    if 'LST_Day' in df_merged.columns.tolist():
        df_merged.rename(columns={'LST_Day' : 'LST_Day_' + str(statics)}, inplace=True)
    else:
        pass
    if 'LST_Night' in df_merged.columns.tolist():
        df_merged.rename(columns={'LST_Night' : 'LST_Night_' + str(statics)}, inplace=True)
    else:
        pass
    if 'LST_Mean' in df_merged.columns.tolist():
        df_merged.rename(columns={'LST_Mean' : 'LST_Mean_' + str(statics)}, inplace=True)
    else:
        pass

    df_merged.to_csv(session['user_id'] + '/final.csv', index=False)


#Combine date csv files and combine them according to different statistical values.

def cbind_Modis_Nadir(statics):

    all_files = glob.glob(os.path.join(session['user_id'],"Modis_Nadir_{}*.csv".format(statics)))

    df_from_each_file = (pd.read_csv(f, sep = ",") for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index = True)
    if 'ndvi' in df_merged.columns.tolist():
        df_merged.rename(columns={'ndvi' : 'NDVI_' + str(statics)}, inplace = True)
    else:
        pass
    if 'evi' in df_merged.columns.tolist():
        df_merged.rename(columns={'evi' : 'EVI_' + str(statics)}, inplace = True)
    else:
        pass
    if 'savi' in df_merged.columns.tolist():
        df_merged.rename(columns={'savi' : 'SAVI_' + str(statics)}, inplace = True)
    else:
        pass
    if 'NDWI_Gao' in df_merged.columns.tolist():
        df_merged.rename(columns={'NDWI_Gao' : 'NDWI_Gao_' + str(statics)}, inplace = True)
    else:
        pass
    if 'NDWI_Mc' in df_merged.columns.tolist():
        df_merged.rename(columns={'NDWI_Mc' : 'NDWI_Mc_' + str(statics)}, inplace = True)
    else:
        pass
    if 'MNDWI' in df_merged.columns.tolist():
        df_merged.rename(columns={'MNDWI' : 'MNDWI_' + str(statics)}, inplace = True)
    else:
        pass

    df_merged.to_csv(session['user_id'] + '/final.csv', index=False)
