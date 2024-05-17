from datetime import datetime
from app.blueprints import main

@main.app_template_filter()
def string_to_date(value) :
    date_object = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f%z")
    return date_object

