from app import app
from datetime import datetime

@app.template_filter()
def string_to_date(value) :
    date_object = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f%z")
    return date_object

