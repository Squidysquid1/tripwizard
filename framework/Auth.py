import functools

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

class site():
    def __init__(self, siteName, siteDesc, siteTime, siteCost, siteAddress, siteCategory):
        self.__name = siteName
        self.__desc = siteDesc
        self.__time = siteTime
        self.__cost = siteCost
        self.__address = siteAddress
        self.__category = siteCategory

    def get_name(self):
        return self.__name
    
    def get_desc(self):
        return self.__desc

    def get_time(self):
        return self.__time
    
    def get_cost(self):
        return self.__cost

    def get_address(self):
        return self.__address

    def get_category(self):
        return self.__category

class day():
    def __init__(self, site1, site2, site3, site4, site5, site6):
        self.__s1 = site1
        self.__s2 = site2
        self.__s3 = site3
        self.__s4 = site4
        self.__s5 = site5
        self.__s6 = site6
    
    def get_s1(self):
        return self.__s1
    
    def get_s2(self):
        return self.__s2
    
    def get_s3(self):
        return self.__s3
    
    def get_s4(self):
        return self.__s4
    
    def get_s5(self):
        return self.__s5
    
    def get_s6(self):
        return self.__s6
    
    def time_converter(self, timeNum):
        time = timeNum
        timeString = str(time)
        length = len(timeString)

        if length == 4:
            hour = timeString[0-1]
            minute = timeString[2-3]


    
    def fullDayInformation(self):
        time = 850
        '''Leave hotel at 8:30'''
        '''Add a place to display time'''
    
class Itinerary:
    def __init__(self, day1, day2, day3, day4):
        self.__d1 = day1
        self.__d2 = day2
        self.__d3 = day3
        self.__d4 = day4