from random import Random
from datetime import timedelta, datetime

import shapefile
import logging


def _last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)


def monthlist(begin,end):
    # begin = datetime.strptime(begin, "%Y-%m-%d")
    # end = datetime.strptime(end, "%Y-%m-%d")

    result = []
    while True:
        if begin.month == 12:
            next_month = begin.replace(year=begin.year+1,month=1, day=1)
        else:
            next_month = begin.replace(month=begin.month+1, day=1)
        if next_month > end:
            break
        result.append ([begin.strftime("%Y-%m-%d"),_last_day_of_month(begin).strftime("%Y-%m-%d")])
        begin = next_month
    result.append ([begin.strftime("%Y-%m-%d"),end.strftime("%Y-%m-%d")])
    return result


def date_format_concersion(date, output_format='%Y/%m/%d'):

    # Fool-proof: check if the input date is None
    if date is None:
        return None

    try: 
        parsed_date = datetime.strptime(date, output_format)
        
    except ValueError as e:

        try:
            # Try to parse the input date
            parsed_date = datetime.strptime(date, '%Y%m%d')
        except ValueError as e:
        
            try:
                parsed_date = datetime.strptime(date, '%Y_%m_%d')
            except ValueError as e:

                try:
                    parsed_date = datetime.strptime(date, '%Y-%m-%d')
                except ValueError as e:

                    return logging.error(f'Unparsable date format {e}')

    output_date = parsed_date.strftime(output_format)

    return output_date


def get_shapefile_fields(shapefile_path):
    shp = shapefile.Reader(shapefile_path)

    # Skip the first field, which is typically 'DeletionFlag'
    shp_fields = [field[0] for field in shp.fields[1:]]
    return shp_fields