from flask import render_template, request, redirect, url_for, session, Blueprint
from view_form_new import ProductForm
from werkzeug.utils import secure_filename
from setting.config import settings
from product_routes import routes_product

import logging
import os
import uuid

logger = logging.getLogger(__name__)

routes = Blueprint('routes', __name__,
                   template_folder='templates', static_folder='static')

routes.register_blueprint(routes_product)


def create_user_folder(session):
    """Create a unique user folder for each session."""

    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session)
    absolute_user_folder = os.path.abspath(user_folder)

    return absolute_user_folder


def save_files(files, user_folder):
    """Save files to the user folder."""

    for file in files:
        file.save(os.path.join(user_folder, secure_filename(file.filename)))


def get_product_route(form):
    """Get the route based on the selected product."""
    
    product = str(form.satellite_products.data)

    for _, setting_product in enumerate(settings.satellite_products_list):
        if product == setting_product:
            return f"routes.routes_product.{settings.satellite_products_list[setting_product]}"

    return None


@routes.route('/zonal_index', methods=['GET', 'POST'])
def zonal_index():

    form = ProductForm(request.form)
    session['user_id'] = str(uuid.uuid4())
    user_folder = create_user_folder(session['user_id'])
    os.makedirs(user_folder)

    if request.method == 'POST':

        return redirect(url_for('zonal_all'))

    return render_template('Zonal_Index.html', form=form)


@routes.route('/zonal_all', methods=['GET', 'POST'])
def zonal_all():

    form = ProductForm(request.form)
    user_folder = create_user_folder(session['user_id'])
    save_files(request.files.getlist('file'), user_folder)

    if request.method == 'POST':
        product_route = get_product_route(form)
        if product_route:
            return redirect(url_for(product_route, form=form))

    return render_template('Zonal_Index.html', form=form)
