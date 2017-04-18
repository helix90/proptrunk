from flask import Blueprint

inventory = Blueprint('auth', __name__)

from . import views
