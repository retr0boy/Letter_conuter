from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
wsgi_app = app.wsgi_app
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes