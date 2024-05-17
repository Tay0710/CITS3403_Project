from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'home'

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.blueprints import main
    app.register_blueprint(main)
    db.init_app(app)
    login.init_app(app)
    
    return app

moment = Moment(app)

from app import routes, models, errors, filters