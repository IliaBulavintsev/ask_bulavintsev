# import multiprocessing

bind = ['127.0.0.1:8001']
workers = 2
pidfile = 'gunicorn_pid'
daemon = True
access = 'logs/gunicorn_access.log'
error = 'logs/gunicorn_error.log'
