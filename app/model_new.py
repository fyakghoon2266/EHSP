from flask import session, request, Blueprint
from random import Random
from datetime import timedelta, datetime
from view_form import ProductForm
from app.setting import utl

routes = Blueprint('routes', __name__)
