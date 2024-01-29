from flask import Flask, request, redirect, render_template, url_for, Blueprint, session
from flask_session import Session
from view_form_new import ProductForm
from setting.config import settings
from setting.utl import get_shapefile_fields
from routes_model import routes_model

import shapefile
import glob
import os


routes_product = Blueprint('routes_product', __name__)

routes_product.register_blueprint(routes_model)


@routes_product.route('/product_chirsp', methods=['GET', 'POST'])
async def chirsp():

    form = ProductForm(request.form)
    shp_filed = get_shapefile_fields("".join(glob.glob(os.path.join(session['user_id'],'*.shp'))))

    form.regional_category.choices = shp_filed

    #  The flask_wtf class provides a method for judging whether the form has been submitted. 
    #  You do not need to use request.method to make the judgment yourself.
    if form.validate_on_submit():

        return redirect(url_for('routes.Model_Chirsp', form=form))

    return render_template('Chirsp.html', form=form)
