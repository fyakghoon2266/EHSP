from flask import render_template, request, redirect, url_for, session, Blueprint, send_file
from random import Random
from datetime import timedelta, datetime
from view_form_new import ProductForm
from setting import utl
from setting.utl import str_random

routes = Blueprint('routes', __name__)


@routes.route('/zonal_index', methods=['GET', 'POST'])
def zonal_index():
    form = ProductForm()

    if request.method == 'POST':
        # 在这里处理表单提交，使用 request.form 获取表单数据
        # ...

        return redirect(url_for('zonal_all'))  # 不再传递 form 参数

    return render_template('Zonal_Index.html', form=form)

@routes.route('/zonal_all')
def zonal_all():
    # 处理 zonal_all 的逻辑
    return 'Zonal All Page'