# Configuration file for ipython.

c = get_config()

c.InteractiveShellApp.exec_lines = [
    '%load_ext autoreload',
    '%autoreload 2',
    'from source.app import create_app',
    'create_app().app_context().push()',
]
