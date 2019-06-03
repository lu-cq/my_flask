# coding: utf-8
import sys
import logging

from flask import Flask
from werkzeug.utils import import_string
from libs.logger.filelogger import get_file_logger
from tasks import make_celery


blueprints = [
    'src.middlewares.cross_domain:bp',
    'src.middlewares.auto_commit:bp',
    'src.views.api.v1.order:bp',
]

extensions = [
    'source.ext:db',
]

collected_loggers = [
    ('libs.ali_id_card.client', logging.INFO),
]
celery_tasks = [
    'tasks.order',
]

CELERY = None


def create_app(config=None):
    """Create application cmstance."""
    app = Flask(__name__)

    app.config.from_object('envcfg.json.flask')
    app.config.from_object(config)
    global CELERY
    CELERY = make_celery(app)

    for extension_qualname in extensions:
        extension = import_string(extension_qualname)
        extension.init_app(app)

    for blueprint_qualname in blueprints:
        blueprint = import_string(blueprint_qualname)
        app.register_blueprint(blueprint)

    for logger_name, logger_level in collected_loggers:
        get_file_logger(logger_name)

    for task in celery_tasks:
        import_string(task)

    return app
