import multiprocessing

chdir = '/var/www/django-wedding/'
bind = 'unix:wedding.sock'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 30
command = '/home/ieatkittens/.virtualenvs/wedding/bin/gunicorn'
pythonpath = '/var/www/django-wedding/'
django_settings = 'wedding.settings'
accesslog = '/var/log/gunicorn/gunicorn_access.log'
errorlog  = '/var/log/gunicorn/gunicorn_error.log'
loglevel  = 'debug'
user = 'www-data'
