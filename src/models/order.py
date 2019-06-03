# coding: utf-8
from werkzeug.utils import cached_property
from sqlalchemy import func, text, Index

from src.ext import db
from src.models.base import BaseModel
from src.models.user import User


class Order(db.Model, BaseModel):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, nullable=False, server_default='0', index=True, comment='user_id')
    create_time = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    update_time = db.Column(
        db.TIMESTAMP, nullable=False,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )

    def __getattr__(self, item):
        return getattr(self.user, item)

    @property
    def user(self):
        return User.get(self.user_id)
