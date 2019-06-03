# coding: utf-8

from __future__ import absolute_import

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gunicorn.app.wsgiapp import WSGIApplication

from src.ext import db
from src.wsgi import app


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return {'db': db, 'app': app}


@manager.command
def runserver(host=None, port=None, workers=None):
    """Runs the app within Gunicorn."""
    host = host or app.config.get('HTTP_HOST') or '0.0.0.0'
    port = port or app.config.get('HTTP_PORT') or 5000
    workers = workers or app.config.get('HTTP_WORKERS') or 1
    use_evalex = app.config.get('USE_EVALEX', app.debug)

    if app.debug:
        app.run(host, int(port), use_evalex=use_evalex)
    else:
        gunicorn = WSGIApplication()
        gunicorn.load_wsgiapp = lambda: app
        gunicorn.cfg.set('bind', '%s:%s' % (host, port))
        gunicorn.cfg.set('workers', workers)
        gunicorn.cfg.set('pidfile', None)
        gunicorn.cfg.set('accesslog', '-')
        gunicorn.cfg.set('errorlog', '-')
        gunicorn.chdir()
        gunicorn.run()


def main():
    manager.run()


if __name__ == '__main__':
    main()
