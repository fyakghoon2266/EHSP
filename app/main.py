from flask import Flask, request, redirect, render_template, url_for, session
from flask_session import Session
from view_form_new import ProductForm
from setting.config import settings
from routes_new import routes

import uuid
import logging
import os

logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# Create the result folder if it doesn't exist
result_folder = os.path.join(os.getcwd(), 'result')
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

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

# @app.teardown_request
# def teardown_request(exception=None):
#     # Clean up resources or perform actions when the request ends
#     user_folder = os.path.join(result_folder, 'user_data', session.get('user_id', ''))
#     if os.path.exists(user_folder):
#         shutil.rmtree(user_folder)


if __name__ == '__main__':
  app.debug = True
  app.run(threaded=True,host="0.0.0.0",port=50000)