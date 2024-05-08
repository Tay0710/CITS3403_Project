# To be able to execute this you need to undertake the following steps:
# 1. create your table in models.py
# 2. flask db init
# 3. flask db migrate
# 4. flask db upgrade
# 5. Should be able to app app.db and see the new database
# NEXT STEP IS TO CONNECT IT TO THE HTML!! SHOULD PROBS COMMIT THIS
# Make sure you've imported the table to routes.py and studiVault.py 

from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import relationship
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    fname: so.Mapped[str] = so.mapped_column(sa.String(64))
    lname: so.Mapped[str] = so.mapped_column(sa.String(64))
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    position: so.Mapped[str] = so.mapped_column(sa.String(64))
    study: so.Mapped[str] = so.mapped_column(sa.String(64))
    bio: so.Mapped[str] = so.mapped_column(sa.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Questions(db.Model):
    post_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    topic: so.Mapped[str] = so.mapped_column(sa.String(120))
    subtopic: so.Mapped[str] = so.mapped_column(sa.String(120))
    title: so.Mapped[str] = so.mapped_column(sa.String(120))
    description: so.Mapped[str] = so.mapped_column(sa.String(255))

    # Define the relationship with Comments
    comments = relationship('Comments', backref='question')
    
    def __repr__(self):
        return '<Questions {}>'.format(self.title)
    
class Comments(db.Model):
    comment_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    comment_text: so.Mapped[str] = so.mapped_column(sa.Text, nullable=False)
    post_id: so.Mapped[int] = so.mapped_column(sa.Integer, db.ForeignKey('questions.post_id'), nullable=False)

    def __repr__(self):
        return '<Comments {}>'.format(self.text)
