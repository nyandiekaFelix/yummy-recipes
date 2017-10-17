import os
from flask import Flask

app = Flask(__name__)

from yummy_recipes.models import user