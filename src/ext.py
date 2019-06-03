# coding: utf-8

from __future__ import absolute_import

from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer
from envcfg.json.flask import SECRET_KEY, TOKEN_EXPIRES_IN


token_object = TimedJSONWebSignatureSerializer(SECRET_KEY, TOKEN_EXPIRES_IN)
db = SQLAlchemy()
