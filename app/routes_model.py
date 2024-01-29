from flask import render_template, request, redirect, url_for, session, Blueprint
from view_form_new import ProductForm
from werkzeug.utils import secure_filename
from setting.config import settings
from product import routes_product

import logging
import os

logger = logging.getLogger(__name__)

routes_model = Blueprint('routes_model', __name__)