from flask import Flask
from config import config
app = Flask(__name__)
wsgi_app = app.wsgi_app
app.config.from_object(config)
from app import routes