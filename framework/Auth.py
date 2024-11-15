import functools
import random

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


'''@bp.route("/survey", methods=("GET", "POST"))
def generate_itinerary():
   country = request.form.get('country')
   city = request.form.get('city')
   days = request.form.get('days')
   categories = request.form.getlist('category')
   busyness = request.form.get('busyness')

   # Implement the logic to generate itinerary based on inputs
   itinerary = create_itinerary(country, city, days, categories, busyness)

   return render_template('itinerary.html', itinerary=itinerary)'''



