import functools
import random

'''The code that used to be here was written by Anita, before we ditched the account feature because we wanted to focus on other parts. '''

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import random
from .Database import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

