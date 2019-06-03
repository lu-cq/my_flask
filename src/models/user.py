# coding: utf-8
from sqlalchemy import func, text, Index

from src.ext import db
from src.models.base import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, server_default='', comment='姓名')
    create_time = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    update_time = db.Column(
        db.TIMESTAMP, nullable=False,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
