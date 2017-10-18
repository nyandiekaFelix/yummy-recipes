from flask import Flask
from flask_wtf.csrf import CSRFProtect

APP = Flask(__name__)
APP.secret_key = 'very_secret' # to be set as env variale later
csrf = CSRFProtect(APP)

from yummy_recipes import views
