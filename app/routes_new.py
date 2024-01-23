from flask import render_template, request, redirect, url_for, session, Blueprint, send_file
from random import Random
from datetime import timedelta, datetime
from view_form_new import ProductForm
from setting import utl
from setting.utl import str_random
from werkzeug.utils import secure_filename
from setting.config import settings

import logging
import os

logger = logging.getLogger(__name__)

routes = Blueprint('routes', __name__, template_folder='templates', static_folder='static')

@routes.route('/zonal_index', methods=['GET', 'POST'])
def zonal_index():
    form = ProductForm()

    if 'user_id' not in session:
        session['user_id'] = str_random()
        logger.info(session['user_id'])

    if request.method == 'POST':
        # Form submission is handled here, and request.form is used to obtain form data.
        # ...

        return redirect(url_for('zonal_all'))  # No more passing form parameters

    return render_template('Zonal_Index.html', form=form)

@routes.route('/zonal_all', methods=['GET', 'POST'])
def zonal_all():
    form = ProductForm()

    if os.path.isdir(session['user_id']) == True:
        logger.info(f"User {session['user_id']} folder already exists")
    else:
        os.makedirs(session['user_id'])

    # for file in request.files.getlist('file'):
    #     file.save(os.path.join(session['user_id'], secure_filename(file.filename)))

    if request.method == 'POST':
        
        if str(form.satellite_products.data) == str(settings.satellite_products_list[0]):
            return redirect(url_for('routes_zonal.chirsp', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[1]):
            return redirect(url_for('routes_zonal.ear5', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[2]):
            return redirect(url_for('routes_zonal.modis_ndvi_evi', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[3]):
            return redirect(url_for('routes_zonal.modis_lst', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[4]):
            return redirect(url_for('routes_zonal.modis_nadir', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[5]):
            return redirect(url_for('routes_zonal.strm_elevation', form=form))
        
    return render_template('Zonal_All.html', form=form)