from flask import Flask, request, redirect, render_template, url_for, Blueprint, session
from flask_session import Session
from view_form_new import ProductForm
from setting.config import settings

routes = Blueprint('routes', __name__)

@routes.route('/zonal_index', methods=['GET', 'POST'])
async def zonal_index():

    form = ProductForm
