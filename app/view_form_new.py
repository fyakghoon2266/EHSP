from flask_wtf import FlaskForm
from setting.config import settings
from numpy import str0
import wtforms as wtf

# from class flaskform

class ProductForm(FlaskForm):

    satellite_products = wtf.RadioField(
        '',
        choices=list(settings.satellite_products_list.keys()),
        validators=[
            wtf.validators.DataRequired(message=settings.message)
            ]
    )

    product_type = wtf.RadioField(
        'select output format',
        choices=settings.product_type_list,
        validators=[
            wtf.validators.DataRequired(message=settings.message)
            ]
    )

    start_date = wtf.DateField(
        'start Date',
        validators=[
            wtf.validators.DataRequired(message=settings.message)
        ]
    )

    end_date = wtf.DateField(
        'End Date',
        validators=[
            wtf.validators.DataRequired(message=settings.message)
        ]
    )

    chrisp_bands = wtf.SelectMultipleField(
        settings.bands_introduction,
        choices=settings.chrisp_bands_list,
        validators=[
            wtf.validators.DataRequired(message=settings.message)
            ]
    )

    era5_bands = wtf.SelectMultipleField(
        settings.bands_introduction,
        choices=settings.era5_bands_list,
        validators=[
            wtf.validators.DataRequired(message=settings.message)
        ]
    )

    modis_ndvi_evi_bands = wtf.SelectMultipleField(
        settings.bands_introduction,
        choices=settings.modis_ndvi_evi_bands_list,
        validators=[
            wtf.validators.DataRequired(message=settings.message)
        ]
    )

    modis_lst_bands = wtf.SelectMultipleField(
        settings.bands_introduction,
        choices=settings.modis_lst_bands_list,
        validators=[
            wtf.validators.DataRequired(message=settings.message)
        ]
    )

    modis_nadir_bands = wtf.SelectMultipleField(
        settings.bands_introduction,
        choices=settings.modis_nadir_bands_list,
        validators=[
            wtf.validators.DataRequired(message=settings.message)
        ]
    )

    shp = wtf.MultipleFileField(
        settings.shp_name,
        validators=[wtf.validators.DataRequired(message=settings.message)]
    )

    regional_category = wtf.SelectField(settings.regional_category, coerce=str0)

    statics = wtf.SelectField(settings.statistic_name, choices=settings.statistic_list)

    statics_world_cover = wtf.SelectField(settings.statistic_name, choices=settings.statics_world_list)

    submit = wtf.SubmitField('Submit')