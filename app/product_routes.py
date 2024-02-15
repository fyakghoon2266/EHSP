from flask import request, redirect, render_template, url_for, Blueprint, session
from view_form_new import ProductForm
from setting.utl import get_shapefile_fields
from model_routes import routes_model

import glob
import os


routes_product = Blueprint('routes_product', __name__, template_folder='templates', static_folder='static')

routes_product.register_blueprint(routes_model)


@routes_product.route('/product_chirsp', methods=['GET', 'POST'])
async def chirsp():

    form = ProductForm(request.form)

    result_folder = os.path.join(os.getcwd(), 'result')
    user_folder = os.path.join(result_folder, 'user_data', session['user_id'])

    shp_filed = get_shapefile_fields("".join(glob.glob(os.path.join(user_folder, '*.shp'))))

    form.regional_category.choices = shp_filed

    #  The flask_wtf class provides a method for judging whether the form has been submitted. 
    #  You do not need to use request.method to make the judgment yourself.
    if request.method == 'POST':
        return redirect(url_for('routes.routes_product.routes_model.model_chirsp', form=form))

    return render_template('Chirsp.html', form=form)
