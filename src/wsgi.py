# -*- coding: UTF-8 -*-
# from envcfg.json.cms import DEBUG
# if not DEBUG:
#     from gevent import monkey
#     monkey.patch_all(thread=False)

from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.middleware.profiler import ProfilerMiddleware
# from werkzeug.contrib.profiler import ProfilerMiddleware

from .app import create_app

__all__ = ['app']

#: WSGI endpoint
app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

if app.config.get('PROFILING', False):
    app.wsgi_app = ProfilerMiddleware(
        app.wsgi_app, profile_dir=app.config['PROFILING_DIR'])
