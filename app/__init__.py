from flask import Flask

app = Flask(__name__, static_folder = 'static', static_url_path='')
app.config.from_object('config')

from app import index