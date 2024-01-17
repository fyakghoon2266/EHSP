from flask_wtf import FlaskForm, FileAllowed, FileField, FileRequired
from wsgiref.validate import validator
from app.setting.config import Settings
import wtforms as wtf

# from class flaskform

class ProductForm(FlaskForm):

    satellite_products = wtf.RadioField(
        '',
        choices=Settings.satellite_products,
        validators=[
            wtf.validators.DataRequired(message=Settings.message)
            ]
    )

    product_type = wtf.RadioField(
        'select output format',
        choices=Settings.product_type,
        validators=[
            wtf.validators.DataRequired(message=Settings.message)
            ]
    )

    start_date = wtf.DateField(
        'start Date',
        validators=[
            wtf.validators.DataRequired(message=Settings.message)
        ]
    )

    end_date = wtf.DateField(
        'End Date',
        validators=[
            wtf.validators.DataRequired(message=Settings.message)
        ]
    )

    chrisp_bands = wtf.SelectMultipleField(
        'Environmental Parameters',
        choices=Settings.chrisp_bands_list,
        validators=[
            wtf.validators.DataRequired(message=Settings.message)
            ]
    )