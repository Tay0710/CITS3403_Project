import os
basedir = os.path.abspath(os.path.dirname(__file__))
# suggest changing the name of database_url to have website in front
class Config:
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')