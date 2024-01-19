from flask import Flask, request, redirect, render_template, url_for
from routes import routes
from flask_session import Session
from view_form_new import ProductForm
from app.setting.config import settings

import logging
import os

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.register_blueprint(routes)
SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@routes.route('/', methods=['POST'])
async def index():
	form = ProductForm()

	if request.method == 'POST':

		if str(form.product_type.data) == str(settings.product_type[0]):
			return redirect(url_for('zonal_index', form=form))

		elif str(form.product_type.data) == str(settings.product_type[1]):
			return redirect(url_for('tiff_raster'), form=form)

		else:
			return logger.error('The system has an error on product_type.')

	return render_template('Index.html', form=form)



if __name__ == '__main__':
  app.debug = True
  app.run(threaded=True,host="0.0.0.0",port=50000)