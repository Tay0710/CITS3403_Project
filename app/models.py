import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# To be able to execute this you need to undertake the following steps:
# 1. create your table in models.py
# 2. flask db init
# 3. flask db migrate
# 4. flask db upgrade
# 5. Should be able to app app.db and see the new database
# NEXT STEP IS TO CONNECT IT TO THE HTML!! SHOULD PROBS COMMIT THIS
# Make sure you've imported the table to routes.py and studiVault.py 

class Questions(db.Model):
    post_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    topic: so.Mapped[str] = so.mapped_column(sa.String(120))
    subtopic: so.Mapped[str] = so.mapped_column(sa.String(120))
    title: so.Mapped[str] = so.mapped_column(sa.String(120))
    description: so.Mapped[str] = so.mapped_column(sa.String(255))

    def __repr__(self):
        return '<Questions {}>'.format(self.title)