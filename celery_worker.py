# coding: utf-8
from src.app import create_app

current_app = create_app()
current_app.app_context().push()

from src.app import CELERY
