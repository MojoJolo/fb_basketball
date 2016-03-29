CSRF_ENABLED = True
SECRET_KEY = 'parokya ni edgar'

# gunicorn -w 1 --log-level info --log-file=- run:app -b 0.0.0.0:8000