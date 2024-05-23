from flask import session, request, Blueprint
from view_form_new import ProductForm
from setting.config import settings
from datetime import timedelta, datetime
from setting.utl import monthlist, date_format_concersion

import cbind as bd
import pandas as pd
import glob
import geemap
import ee
import os


model_routes = Blueprint('model_routes', __name__)

@model_routes.route("/zonal_Chirsp", methods=["POST"])
def zonal_Chirsp():

    # First extract the data provided by the user from the form
    form = ProductForm(request.form)
    
    # star the google earth engine
    service_account = settings.service_account
    credentials = ee.ServiceAccountCredentials(service_account, settings.service_json)
    
    # google earth engine initialization
    ee.Initialize(credentials)
    
    # time division function
    time_list = monthlist(form.start_date.data, form.end_date.data)


    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])
    states = geemap.shp_to_ee("".join(glob.glob(os.path.join(user_folder, '*.shp'))))

    for i in range(0, len(time_list)):
        Chirsp = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY') \
                .filter(ee.Filter.date(datetime.strptime(time_list[i][0], "%Y-%m-%d"), datetime.strptime(time_list[i][1],"%Y-%m-%d")+timedelta(days=1))) \
                .map(lambda image: image.select(list(form.chrisp_bands.data))) \
                .map(lambda image: image.clip(states)) \
                .map(lambda image: image.reproject(crs=settings.crs))

        
        Chirsp = Chirsp.toBands()
        out_dir = os.path.expanduser(user_folder)
        out_dem_stats = os.path.join(out_dir, 'Prec_{}_{}.csv'.format(form.statics.data,time_list[i]))

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        geemap.zonal_statistics(Chirsp, states, out_dem_stats, statistics_type=form.statics.data, scale=1000)

        data_temp = pd.read_csv(out_dem_stats)

        data = []

        if time_list[i][0] == time_list[i][1]:

            df = data_temp
            df[form.regional_category.data] = data_temp.loc[:,[form.regional_category.data]]
            df['Date'] = date_format_concersion(time_list[i][0], output_format='%Y/%m/%d')
            df['Doy'] = datetime.strptime(time_list[i][0], '%Y-%m-%d').strftime('%j')
            select_columns = ['Date', 'Doy'] + [item.lower() for item in [form.statics.data]] + [form.regional_category.data]
            df = df[select_columns]
            new_columns = ['Date', 'Doy'] + form.chrisp_bands.data + [form.regional_category.data]
            df.columns = new_columns

            data.append(df)

        else:
            for j in range(0, len(data_temp.columns), len([form.chrisp_bands.data])):
                date_str = data_temp.columns[j][:8]

                if all(m.isdigit() for m in date_str):

                    df = data_temp.iloc[:, j:j + len([form.chrisp_bands.data])]
                    df[form.regional_category.data] = data_temp.loc[:,[form.regional_category.data]]
                    df['Date'] = date_format_concersion(date_str, output_format='%Y/%m/%d')
                    df['Doy'] = datetime.strptime(date_str, '%Y%m%d').strftime('%j')
                    select_columns = ['Date', 'Doy'] + [data_temp.columns[j]] + [form.regional_category.data]
                    df = df[select_columns]
                    new_columns = ['Date', 'Doy'] + list(form.chrisp_bands.data) + [form.regional_category.data]
                    df.columns = new_columns

                    data.append(df)
                
                else:
                    continue

        appended_data = pd.concat(data, axis=0, ignore_index=True)

        appended_data.to_csv(out_dem_stats, index=False) #Output the file with date and doy back

    bd.cbind_chirsp(form.statics.data, user_folder)


@model_routes.route("/zonal_Era5", methods=["POST"])
def zonal_Era5():

    # First extract the data provided by the user from the form
    form = ProductForm(request.form)
    
    # star the google earth engine
    service_account = settings.service_account
    credentials = ee.ServiceAccountCredentials(service_account, settings.service_json)
    
    # google earth engine initialization
    ee.Initialize(credentials)
    
    # time division function
    time_list = monthlist(form.start_date.data, form.end_date.data)


    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])
    states = geemap.shp_to_ee("".join(glob.glob(os.path.join(user_folder, '*.shp'))))

    for i in range(0, len(time_list)):
        Era5 = ee.ImageCollection('ECMWF/ERA5_LAND/DAILY_AGGR') \
                .filter(ee.Filter.date(datetime.strptime(time_list[i][0], "%Y-%m-%d"), datetime.strptime(time_list[i][1],"%Y-%m-%d")+timedelta(days=1))) \
                .map(lambda image: image.select(list(form.era5_bands.data))) \
                .map(lambda image: image.clip(states)) \
                .map(lambda image: image.reproject(crs=settings.crs))

        
        Era5 = Era5.toBands()
        out_dir = os.path.expanduser(user_folder)
        out_dem_stats = os.path.join(out_dir, 'Era5_{}_{}.csv'.format(form.statics.data,time_list[i]))

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        geemap.zonal_statistics(Era5, states, out_dem_stats, statistics_type=form.statics.data, scale=1000)

        data_temp = pd.read_csv(out_dem_stats)

        data = []

        if (len(form.era5_bands.data)) == 1 & (time_list[i][0] == time_list[i][1]):

            df = data_temp
            df[form.regional_category.data] = data_temp.loc[:,[form.regional_category.data]]
            df['Date'] = date_format_concersion(time_list[i][0], output_format='%Y/%m/%d')
            df['Doy'] = datetime.strptime(time_list[i][0], '%Y-%m-%d').strftime('%j')
            select_columns = ['Date', 'Doy'] + [item.lower() for item in [form.statics.data]] + [form.regional_category.data]
            df = df[select_columns]
            new_columns = ['Date', 'Doy'] + form.era5_bands.data + [form.regional_category.data]
            df.columns = new_columns

            data.append(df)

        else:
            column_name_list = data_temp.columns.tolist()
            c = []
            d = []
            for k in zip(column_name_list[:]):
                c.append(k[0][0:8])
                d.append(k[0])

            data = []
            for j in range(0, len(column_name_list), len(form.era5_bands.data)):

                # 检查日期格式并提取数据
                if all(m.isdigit() for m in c[j:j+len(form.era5_bands.data)]) == True:
                    
                    # 提取数据
                    df = data_temp.loc[:, d[j:j+len(form.era5_bands.data)]]
                    df[form.regional_category.data] = data_temp.loc[:, [form.regional_category.data]]
                                    
                    # 创建新的日期和DOY列
                    df.insert(0, 'Date', '')
                    df['Date'] = date_format_concersion(time_list[i][0], output_format='%Y/%m/%d')
                    
                    df.insert(1, 'Doy', '')
                    df['Doy'] = datetime.strptime(time_list[i][0], '%Y-%m-%d').strftime('%j')
                    
                    # 重命名列
                    colnames = ['Date', 'Doy']
                    colnames.extend(list(form.era5_bands.data))
                    colnames.append(form.regional_category.data)
                    df.columns = [colnames]
                    
                    data.append(df)
                else:
                    continue

        appended_data = pd.concat(data, axis=0, ignore_index=True)

        appended_data.to_csv(out_dem_stats, index=False) #Output the file with date and doy back

    bd.cbind_era5(form.statics.data)


@model_routes.route("/zonal_Modis_NDVI_EVI", methods=["POST"])
def zonal_Modis_NDVI_EVI():

    def _maskModisQA(image):
        qa = image.select('SummaryQA')
        MODLAND_QA_Bits = 1<<1
        mask = qa.bitwiseAnd(MODLAND_QA_Bits).eq(0)
        return image.updateMask(mask).divide(10000)

    # First extract the data provided by the user from the form
    form = ProductForm(request.form)
    
    # star the google earth engine
    service_account = settings.service_account
    credentials = ee.ServiceAccountCredentials(service_account, settings.service_json)
    
    # google earth engine initialization
    ee.Initialize(credentials)
    
    # time division function
    time_list = monthlist(form.start_date.data, form.end_date.data)


    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])
    states = geemap.shp_to_ee("".join(glob.glob(os.path.join(user_folder, '*.shp'))))

    for i in range(0, len(time_list)):
        Modis_NDVI_EVI = ee.ImageCollection('MODIS/061/MOD13Q1') \
                .filter(ee.Filter.date(datetime.strptime(time_list[i][0], "%Y-%m-%d"), datetime.strptime(time_list[i][1],"%Y-%m-%d")+timedelta(days=1))) \
                .filterBounds(states) \
                .map(_maskModisQA) \
                .select(list(form.modis_ndvi_evi_bands.data)) \
                .map(lambda image: image.clip(states))

        
        Modis_NDVI_EVI = Modis_NDVI_EVI.toBands()
        out_dir = os.path.expanduser(user_folder)
        out_dem_stats = os.path.join(out_dir, 'Modis_NDVI_EVI_{}_{}.csv'.format(form.statics.data,time_list[i]))

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        geemap.zonal_statistics(Modis_NDVI_EVI, states, out_dem_stats, statistics_type=form.statics.data, scale=1000)

        data_temp = pd.read_csv(out_dem_stats)

        data = []

        if (len(form.modis_ndvi_evi_bands.data)) == 1 & (time_list[i][0] == time_list[i][1]):

            df = data_temp
            df[form.regional_category.data] = data_temp.loc[:,[form.regional_category.data]]
            df['Date'] = date_format_concersion(time_list[i][0], output_format='%Y/%m/%d')
            df['Doy'] = datetime.strptime(time_list[i][0], '%Y-%m-%d').strftime('%j')
            select_columns = ['Date', 'Doy'] + [item.lower() for item in [form.statics.data]] + [form.regional_category.data]
            df = df[select_columns]
            new_columns = ['Date', 'Doy'] + form.modis_ndvi_evi_bands.data + [form.regional_category.data]
            df.columns = new_columns

            data.append(df)

        else:
            column_name_list = data_temp.columns.tolist()
            c = []
            d = []
            for k in zip(column_name_list[:]):
                c.append(k[0][0:8])
                d.append(k[0])

            data = []
            for j in range(0, len(column_name_list), len(form.modis_ndvi_evi_bands.data)):

                # 检查日期格式并提取数据
                if all(m.isdigit() for m in c[j:j+len(form.modis_ndvi_evi_bands.data)]) == True:
                    
                    # 提取数据
                    df = data_temp.loc[:, d[j:j+len(form.modis_ndvi_evi_bands.data)]]
                    df[form.regional_category.data] = data_temp.loc[:, [form.regional_category.data]]
                                    
                    # 创建新的日期和DOY列
                    df.insert(0, 'Date', '')
                    df['Date'] = date_format_concersion(time_list[i][0], output_format='%Y/%m/%d')
                    
                    df.insert(1, 'Doy', '')
                    df['Doy'] = datetime.strptime(time_list[i][0], '%Y-%m-%d').strftime('%j')
                    
                    # 重命名列
                    colnames = ['Date', 'Doy']
                    colnames.extend(list(form.modis_ndvi_evi_bands.data))
                    colnames.append(form.regional_category.data)
                    df.columns = [colnames]
                    
                    data.append(df)
                else:
                    continue

        appended_data = pd.concat(data, axis=0, ignore_index=True)

        appended_data.to_csv(out_dem_stats, index=False) #Output the file with date and doy back

    # bd.modis_ndvi_evi(form.statics.data)


    