"""
The flask application package.
"""
import logging
from logging import StreamHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Logging configuration
handler = StreamHandler()
handler.setLevel(logging.INFO)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

Session(app)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'


# IMPORTANT: Flask-Login user loader
@login.user_loader
def load_user(id):
    from FlaskWebProject.models import User
    return User.query.get(int(id))


import FlaskWebProject.views
