from flask import render_template, request, redirect, url_for, session, Blueprint
from view_form_new import ProductForm
from werkzeug.utils import secure_filename
from setting.config import settings
from product_routes import routes_product

import logging
import os
import uuid

logger = logging.getLogger(__name__)

routes = Blueprint('routes', __name__, template_folder='templates', static_folder='static')

routes.register_blueprint(routes_product)


@routes.route('/zonal_index', methods=['GET', 'POST'])
def zonal_index():
    form = ProductForm(request.form)

    # Create a unique user folder for each session
    session['user_id'] = str(uuid.uuid4())
    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])
    absolute_user_folder = os.path.abspath(user_folder)
	
    os.makedirs(absolute_user_folder)

    if request.method == 'POST':
        # Form submission is handled here, and request.form is used to obtain form data.
        # ...

        return redirect(url_for('zonal_all'))  # No more passing form parameters

    return render_template('Zonal_Index.html', form=form)

@routes.route('/zonal_all', methods=['GET', 'POST'])
def zonal_all():
    form = ProductForm(request.form)

    files = request.files.getlist('file')
    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])

    for file in files:
        file.save(os.path.join(user_folder, secure_filename(file.filename)))

    if request.method == 'POST':
        
        if str(form.satellite_products.data) == str(settings.satellite_products_list[0]):
            return redirect(url_for('routes.routes_product.chirsp', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[1]):
            return redirect(url_for('routes_product.ear5', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[2]):
            return redirect(url_for('routes_product.modis_ndvi_evi', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[3]):
            return redirect(url_for('routes_product.modis_lst', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[4]):
            return redirect(url_for('routes_product.modis_nadir', form=form))

        elif str(form.satellite_products.data) == str(settings.satellite_products_list[5]):
            return redirect(url_for('routes_product.strm_elevation', form=form))
        
    return render_template('Zonal_Index.html', form=form)