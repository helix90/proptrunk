from flask import Blueprint

checkout = Blueprint('auth', __name__)

from . import views
