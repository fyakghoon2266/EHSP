from flask import render_template, request, redirect, url_for, session, Blueprint, send_file
from random import Random
from datetime import timedelta, datetime
from view_form_new import ProductForm
from setting import utl
from setting.utl import str_random
from werkzeug.utils import secure_filename

import logging
import os

logger = logging.getLogger(__name__)

routes = Blueprint('routes', __name__)


@routes.route('/zonal_index', methods=['GET', 'POST'])
def zonal_index():
    form = ProductForm()

    if request.method == 'POST':
        # Form submission is handled here, and request.form is used to obtain form data.
        # ...

        return redirect(url_for('zonal_all'))  # No more passing form parameters

    return render_template('Zonal_Index.html', form=form)

@routes.route('/zonal_all')
def zonal_all():
    form = ProductForm()

    if os.path.isdir(session['user_id']) == True:
        logger.info(f"User {session['user_id']} folder already exists")
    else:
        os.makedirs(session['user_id'])

    for file in request.files.getlist('file'):
        file.save(os.path.join(session['user_id'], secure_filename(file.filename)))

    if request.method == 'POST':
        return 


    return 'Zonal All Page'