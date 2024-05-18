import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, create_app
from app.models import User, Questions, Comments

from flask_migrate import Migrate
from config import DeploymentConfig

app = create_app(DeploymentConfig)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Questions': Questions, 'Comments': Comments}
