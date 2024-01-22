from flask import Flask, request, redirect, render_template, url_for, Blueprint
from flask_session import Session
from view_form_new import ProductForm
from setting.config import settings

import logging
import os

logger = logging.getLogger(__name__)

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

routes = Blueprint('routes', __name__)
app.register_blueprint(routes)


@app.route('/', methods=['GET', 'POST'])
def index():
	form = ProductForm()

	if request.method == 'POST':

		if str(form.product_type.data) == str(settings.product_type[0]):
			return redirect(url_for('zonal_index', form=form))

		elif str(form.product_type.data) == str(settings.product_type[1]):
			return redirect(url_for('tiff_raster'), form=form)

		else:
			return render_template('/workpool/gee/templates/Index.html', form=form)

	return render_template('Index.html', form=form)

@app.route('/Table', methods=['GET', 'POST'])
def Table():
    form = ProductForm()
    if request.method == 'POST':

        return render_template('Index.html', form=form)
    return render_template('Table.html', form=form)     


if __name__ == '__main__':
  app.debug = True
  app.run(threaded=True,host="0.0.0.0",port=50000)