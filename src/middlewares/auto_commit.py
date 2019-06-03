# -*- coding: utf-8 -*-

'''
    本地支持跨域
'''

from flask import Blueprint, current_app
from sqlalchemy.exc import SQLAlchemyError

from src.ext import db


bp = Blueprint('middlewares.auto_commit', __name__)


@bp.after_app_request
def auto_commit(response):
    # add for develop mode
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

    return response

