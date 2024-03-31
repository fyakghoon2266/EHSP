from flask import redirect, url_for, session, Blueprint, send_file
from models_new import zonal_Chirsp, zonal_Era5

import shutil
import logging
import os

logger = logging.getLogger(__name__)

routes_model = Blueprint('routes_model', __name__)

@routes_model.route('/model_chirsp', methods=['GET', 'POST'])
async def model_chirsp():

    zonal_Chirsp()

    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])

    if os.path.isfile(user_folder + '/final.csv') == True:
        return redirect(url_for('routes.routes_product.routes_model.download_file'))
    else:
        return('No file exist, Please retry again')


@routes_model.route('/model_era5', methods=['GET', 'POST'])
async def model_era5():

    zonal_Era5()

    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])

    if os.path.isfile(user_folder + '/final.csv') == True:
        return redirect(url_for('routes.routes_product.routes_model.download_file'))
    else:
        return('No file exist, Please retry again')


@routes_model.route('/download_file')
def download_file():

    # 取得下載檔案的路徑
    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])
    filepath = user_folder + '/final.csv'
    
    # 設定下載檔案的資訊
    response = send_file(filepath, mimetype="text/csv", download_name="data.csv")
    
    response.set_cookie('fileDownload', 'true', max_age=20)
    # 刪除資料夾及其內容
    shutil.rmtree(user_folder)
    
    # 回傳下載檔案
    return response