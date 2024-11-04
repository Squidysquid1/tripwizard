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

import random

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
        toMinutes = (3/5)
        timeString = str(time)
        length = len(timeString)
        
        if length == 4:
            hour = int(timeString[0])
            hour *= 10
            hour2 = int(timeString[1])
            hour += hour2
            minute = timeString[2]
            if minute !="0":
                numMinute = int(minute)
                numMinute *= 10
                numMinute2 = int(timeString[3])
                numMinute += numMinute2
                minute = numMinute
                minute *= toMinutes
                minute = round(minute)
            else:
                numMinute2 = int(timeString[3])
                if numMinute2 == 0:
                    minute = "00"
                elif numMinute2 == 1:
                    minute = "01"
                elif numMinute2 == 2:
                    minute = "02"
                elif numMinute2 == 3:
                    minute = "03"
                elif numMinute2 == 4:
                    minute = "04"
                elif numMinute2 == 5:
                    minute = "05"
                elif numMinute2 == 6:
                    minute = "06"
                elif numMinute2 == 7:
                    minute = "07"
                elif numMinute2 == 8:
                    minute = "08"
                elif numMinute2 == 9:
                    minute = "09"
            print(str(hour) + ":" + str(minute))
        else:
            hour = int(timeString[0])
            minute = timeString[1]
            if minute !="0":
                numMinute = int(minute)
                numMinute *= 10
                numMinute2 = int(timeString[2])
                numMinute += numMinute2
                minute = numMinute
                minute *= toMinutes
                minute = round(minute)
            else:
                numMinute2 = int(timeString[2])
                if numMinute2 == 0:
                    minute = "00"
                elif numMinute2 == 1:
                    minute = "01"
                elif numMinute2 == 2:
                    minute = "02"
                elif numMinute2 == 3:
                    minute = "03"
                elif numMinute2 == 4:
                    minute = "04"
                elif numMinute2 == 5:
                    minute = "05"
                elif numMinute2 == 6:
                    minute = "06"
                elif numMinute2 == 7:
                    minute = "07"
                elif numMinute2 == 8:
                    minute = "08"
                elif numMinute2 == 9:
                    minute = "09"
            print(str(hour) + ":" + str(minute))
            

    def fullDayInformation(self):
        happening = "Leave Hotel and go to " + self.__s1.get_name() + ". \n"
        print(happening)
        time = 850
        '''Leave hotel at 8:30'''
        '''Add a place to display time'''
        self.time_converter(time)

        
        happening = "\nArrive at " + self.__s1.get_name() + ". \n"
        print(happening)
        siteOneTime = s1.get_time()
        time += siteOneTime
        self.time_converter(time)
        '''site two accounted for'''

        happening = "\nArrive at " + self.__s2.get_name() + ". \n"
        print(happening)
        siteTwoTime = s2.get_time()
        time += siteTwoTime
        self.time_converter(time)
        '''site 2 accounted for'''

        if s3 != 0:
            happening = "\nArrive at " + self.__s3.get_name() + ". \n"
            print(happening)
            siteThreeTime = s3.get_time()
            time += siteThreeTime
            self.time_converter(time)
            '''site 3 accounted for'''
            if s4 != 0:
                happening = "\nArrive at " + self.__s4.get_name() + ". \n"
                print(happening)
                siteFourTime = s4.get_time()
                time += siteFourTime
                self.time_converter(time)
                '''site 4 accounted for'''
                if s5 != 0:
                    happening = "\nArrive at " + self.__s5.get_name() + ". \n"
                    print(happening)
                    siteFiveTime = s5.get_time()
                    time += siteFiveTime
                    self.time_converter(time)
                    '''site 5 accounted for'''
                    if s6 != 0:
                        happening = "\nArrive at " + self.__s6.get_name() + ". \n"
                        
                        happening = "\nArrive at " + self.__s6.get_name() + ". \n"
                        print(happening)
                        siteSixTime = s6.get_time()
                        time += siteSixTime
                        self.time_converter(time)
                        '''site 6 accounted for'''

                    else:
                        '''no site 6, no more time adjustments'''
                else:
                    '''no site 5, no more time adjustments'''
            else:
                '''no site 4, no more time adjustments'''
        else:
            '''no site 3, no more time adjustments'''

        

        
class itinerary():
    def __init__(self, day1, day2, day3, day4):
        self.__d1 = day1
        self.__d2 = day2
        self.__d3 = day3
        self.__d4 = day4

    def printFullItinerary(self):
        print(self.__d1.fullDayInformation())
        if self.__d2 != 0:
            print(self.__d2.fullDayInformation())
            if self.__d3 != 0:
                print(self.__d3.fullDayInformation())
                if self.__d4 != 0:
                    print(self.__d4.fullDayInformation())
        else:
            '''Dont do anything, there's only one day'''

'''s1 = site("1", "site 1", 150, 1, "address 1", "generic")
s2 = site("2", "site 2", 75, 1, "address 2", "generic")
s3 = site("3", "site 3", 125, 1, "address 3", "generic")
s4 = site("4", "site 4", 200, 1, "address 4", "generic")
s5 = site("5", "site 5", 50, 1, "address 5", "generic")
s6 = site("6", "site 6", 100, 1, "address 6", "generic")
d1 = day(s1, s2, s3, s4, s5, s6)
'''




berlin_sites = []
'''update this count whenever you add a new site.'''
'''8 historical, 2 family, 2 nature, 0 nightlife'''

prison = site("Hohenschoenhausen Prison", "The Hohenschoenhausen Prison is a former East German Prison. Today, former inmates and scholars give tours, recounting the brutal methods used here. While a bit outside the city center, it is a must-see for any tourist.", 200, 8.89, "Genslerstraße 66, 13055 Berlin, Germany", "Historical")
berlin_sites.append(prison)

topography = site("Topography of Terror", "The Topography of Terror Museum describes the horrors of the Nazi regime. It also includes a chunk of the Berlin Wall outside, with plaques describing the history behind it as well.", 150, 0, "Niedderkirchnerstrasse 8, 10963 Berlin, Germany", "Historical")
berlin_sites.append(topography)

charlie = site("Checkpoint Charlie", "Checkpoint Charlie used to be a crossing point along the Berlin Wall. American and Soviet tanks had a standoff here in 1961. Today, it is a recognizable part of Berlin, and an essential site to visit.", 25, 0, "Friedrichstrasse 43-45, 10117 Berlin, Germany", "Historical")
berlin_sites.append(charlie)

reichstag = site("Reichstag Building", "The Reichstag is Germany's Parliment Building. In 1934, this place was burned down, which lead to the Reichstag Fire Decree expanding Hitler's power against communists. Today, it shows its scarred past while maintainting transparency to the public. Tours are an extra cost, but the top part is free to visit.", 225, 0, "Platz der Republik 1, 11011 Berlin, Germany", "Historical")
berlin_sites.append(reichstag)

tv = site("TV Tower", "The TV Tower is an iconic landmark in the Berlin skyline. Built to demonstrate East Germany's technological prowess during the Cold War, it is now a popular tourist attraction that shows a panoramic view of the city. There is a restaurant inside, but it is rather expensive.", 200, 22.50, "Panoramastrasse 1a, Berlin, Germany", "Historical")
berlin_sites.append(tv)

zitadelle = site("Zitadelle", "The Zitadelle is an old fortress that now lies outside of the city. Several exhibits have been set up showcasing not only the fortress's history, but other historical knowledge. It was featured in the movie Gotcha.", 150, 4.50, "Am Juliusturm 64, 13599 Berlin, Germany", "Historical")
berlin_sites.append(zitadelle)

gate = site("Brandenburg Gate", "The Brandenburg Gate is a symbol of Berlin itself. This landmark has stood the test of time, and is now a popular tourist attraction.", 25, 0, "Pariser Platz, 10117 Berlin, Germany", "Historical")
berlin_sites.append(gate)

zoo = site("Berlin Zoo", "The Berlin Zoo is teeming with unique kinds of animals and exhibits, and can be enjoyed by all ages.", 200, 22.99, "Hardenbergplatz 8, 10787 Berlin, Germany", "Family")
berlin_sites.append(zoo)

jewmem = site("Jewish Memorial", "This area full of rectangular stones serves as a memorial for the Jews killed during the Holocaust.", 20, 0, "Cora-Berliner-Straße 1, 10117 Berlin, Germany", "Historical")
berlin_sites.append(jewmem)

mauerpark = site("Mauerpark", "The Mauerpark is a large park near where the Berlin Wall used to be. ", 75, 0, "Bernauer Str. 63, 13355 Berlin, Germany", "Nature")
berlin_sites.append(mauerpark)

viktoriapark = site("Viktoriapark", "The Viktoriapark includes a waterfall, viewing platform, and incredible view of the city of Berlin.", 100, 0, "Katzbachstraße, 10965 Berlin, Germany", "Nature")
berlin_sites.append(viktoriapark)

nathist = site("Museum of Natural History", "The Museum of Natural History is a museum that contains a large collection of natural history artifacts, with exhibits on everything from dinosaurs to marine life.", 150, 11.97, "Invalidenstraße 43, 10115 Berlin, Germany", "Family")
berlin_sites.append(nathist)

site_a = site("site a", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_a)
site_b = site("site b", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_b)
site_c = site("sitec", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_c)
site_d = site("sited", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_d)
site_e = site("sitee", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_e)
site_f = site("sitef", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_f)
site_g = site("siteg", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_g)
site_h = site("siteh", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_h)
site_i = site("sitei", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_i)
site_j = site("sitej", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_j)
site_k = site("sitek", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_k)
site_l = site("sitel", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_l)
site_m = site("sitem", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_m)
site_n = site("siten", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_n)
site_o = site("siteo", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_o)
site_p = site("sitep", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_p)
site_q = site("siteq", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_q)
site_r = site("siter", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_r)
site_s = site("sites", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_s)
site_t = site("sitet", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_t)
site_u = site("siteu", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_u)
site_v = site("sitev", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_v)
site_w = site("sitew", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_w)
site_x = site("sitex", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_x)
site_y = site("sitey", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_y)
site_z = site("sitezz", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_z)
site_aa = site("siteaa", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_aa)
site_ab = site("siteab", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ab)
site_ac = site("siteac", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ac)
site_ad = site("sitead", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ad)
site_ae = site("siteae", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ae)
site_af = site("siteaf", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_af)
site_ag = site("siteag", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ag)
site_ah = site("siteah", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ah)
site_ai = site("siteai", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ai)
site_aj = site("siteaj", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_aj)
site_ak = site("siteak", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ak)
site_al = site("siteal", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_al)
site_am = site("siteam", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_am)
site_an = site("sitean", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_an)
site_ao = site("siteao", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ao)
site_ap = site("siteap", "site", 100, 0, "address", "Historical")
berlin_sites.append(site_ap)


def generate_itinerary(berlin_sites):
    '''This function generates a random itinerary for the user.'''
    '''The values here are just placeholder values for the variables. in reality, these will be obtained from the survey. '''

    days = 3
    busyness = "moderate"
    checked = ["Historical", "Nature"]
    my_sites = []

    for i in berlin_sites:
        cat = i.get_category()
        if cat in checked:
            my_sites.append(i)
    for i in my_sites:
        print(i.get_name())
    '''This is where the itinerary is generated.'''

    totsites = len(my_sites)

    if days == 1:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 6):
                '''Six sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
        elif busyness == "moderate":
            for i in range (1, 4):
                '''Four sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
        elif busyness == "light":
            for i in range (1, 4):
                '''Two sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
        myItinerary = itinerary(d1, 0, 0, 0)
    elif days == 2:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 12):
                '''Six sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
        elif busyness == "moderate":
            for i in range (1, 8):
                '''Four sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
        elif busyness == "light":
            for i in range (1, 4):
                '''Two sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, 0, 0)
    elif days == 3:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 18):
                '''Six sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
            d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
        elif busyness == "moderate":
            for i in range (1, 12):
                '''Four sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
            d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)

        elif busyness == "light":
            for i in range (1, 6):
                '''Two sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
            d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, d3, 0)
    elif days == 4:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 24):
                '''Six sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
            d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
            d4 = day(myPickedSites[18], myPickedSites[19], myPickedSites[20], myPickedSites[21], myPickedSites[22], myPickedSites[23])
        elif busyness == "moderate":
            for i in range (1, 16):
                '''Four sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
            d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
            d4 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], 0, 0)
        elif busyness == "light":
            for i in range (1, 8):
                '''Two sites in a day'''
                randselect = random.randint(1, totsites)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
            d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
            d4 = day(myPickedSites[6], myPickedSites[7], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, d3, d4)

generate_itinerary(berlin_sites)