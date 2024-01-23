from flask import Flask, request, redirect, render_template, url_for, Blueprint, session
# from flask_session import Session
from view_form_new import ProductForm
from setting.config import settings
from setting.utl import str_random
from routes_new import routes


import logging
import os

logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='templates/css')
SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY
# Session(app)
app.register_blueprint(routes)



@app.route('/', methods=['GET', 'POST'])
async def index():
	form = ProductForm()

	if request.method == 'POST':

		if str(form.product_type.data) == str(settings.product_type_list[0]):
			return redirect(url_for('routes.zonal_index'))

		elif str(form.product_type.data) == str(settings.product_type_list[1]):
			return redirect(url_for('tiff_raster'))

		else:
			return logger.error('The system has an error on product_type.')

	return render_template('Index.html', form=form)

@app.route('/Table', methods=['GET', 'POST'])
def Table():
    form = ProductForm()
    if request.method == 'POST':

        return render_template('Index.html')
    return render_template('Table.html')     


if __name__ == '__main__':
  app.debug = True
  app.run(threaded=True,host="0.0.0.0",port=50000)