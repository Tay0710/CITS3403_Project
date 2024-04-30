from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    fname: so.Mapped[str] = so.mapped_column(sa.String(64))
    lname: so.Mapped[str] = so.mapped_column(sa.String(64))
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    position: so.Mapped[str] = so.mapped_column(sa.String(64))
    study: so.Mapped[str] = so.mapped_column(sa.String(64))
    bio: so.Mapped[str] = so.mapped_column(sa.String(200))

    def __repr__(self):
        return '<User {}>'.format(self.username)