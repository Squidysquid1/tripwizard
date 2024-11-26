from flask import Flask, request, render_template
import random
from flask import Blueprint
import sqlite3

'''Berlin Sites Database'''
conn = sqlite3.connect('berlin.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS berlin (
    name,
    desc,
    time,
    cost,
    address,
    category
)
''')
conn.commit()
'''
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Brandenburg Gate', 'Historic landmark and symbol of German unity', 25, 0, 'Pariser Platz, 10117 Berlin', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Reichstag Building', 'The seat of the German Parliament, offering panoramic views of the city from its glass dome (Tours cost extra)', 200, 0, 'Platz der Republik 1, 11011 Berlin', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Berlin Wall Memorial', 'Bernauer Straße 111, 13355 Berlin', 150, 0, 'A poignant reminder of the Cold War, showcasing the history of the Berlin Wall', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Checkpoint Charlie', 'Friedrichstraße 43-45, 10969 Berlin', 25, 0, 'A former border crossing point between East and West Berlin during the Cold War', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Berlin Cathedral', 'Am Lustgarten, 10178 Berlin', 150, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('East Side Gallery', 'Mühlenstraße 84-130, 10243 Berlin', 75, 0, 'The longest remaining section of the Berlin Wall, adorned with colorful murals', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Potsdamer Platz', 'Potsdamer Platz, 10963 Berlin', 150, 0, 'A vibrant square with modern architecture, shopping malls, and entertainment venues', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('Charlottenburg Palace', 'Spandauer Damm 10-22, 14059 Berlin', 250, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
cursor.execute('INSERT INTO berlin (name, desc, time, cost, address, category) VALUES (?, ?, ?, ?, ?, ?)', ('', '', 0, 0, '', 'historical'))
'''
'''Blueprint'''
bp = Blueprint("survey", __name__)

'''Site Class, Day Class, and Itinerary Class'''
class site():
  def __init__(self, siteName, siteDesc, siteTime, siteCost, siteAddress, siteCategory):
      self.__name = siteName
      self.__desc = siteDesc
      self.__time = siteTime
      self.__cost = siteCost
      self.__address = siteAddress
      self.__category = siteCategory

  def get_name(self):
      stri = str(self.__name)
      return stri

  def get_desc(self):
      stri = str(self.__desc)
      return stri

  def get_time(self):
      return self.__time

  def get_cost(self):
      stri = "Cost: $"
      stri += self.__cost
      return stri

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
        time = str(hour) + ":" + str(minute) + ":"
        return time
            

    def fullDayInformation(self):
        '''Leave hotel: Start of Day'''
        time = 850
        happening = str(self.time_converter(time))
        happening += "\t\t"
        happening += "Leave Hotel and go to " + self.__s1.get_name() + ". \n"
        time += 50

        '''Arrive at Site 1'''
        happening += str(self.time_converter(time))
        happening += "\nArrive at " + self.__s1.get_name() + ". \n"
        s1desc = self.__s1.get_desc()
        happening += s2desc
        '''Display Address so user can get the route'''
        happening += "Address: "
        s1address = self.__s1.get_address()
        happening += s1address
        happening += "\n\n"
        '''Account for time spent at the site'''
        time += self.__s1.get_time()

        '''Leave Site 1, go to Site 2'''
        happening += str(self.time_converter(time))
        happening += "\nLeave " + self.__s1.get_name() + " and go to " + self.__s2.get_name()
        time += 50

        '''Arrive at Site 2'''
        happening += str(self.time_converter(time))
        happening += "\nArrive at " + self.__s2.get_name() + ". \n"
        s2desc = self.__s2.get_desc()
        happening += s2desc
        '''Display Address so user can get the route'''
        happening += "Address: "
        s1address = self.__s1.get_address()
        happening += s1address
        happening += "\n\n"
        '''Account for time spent at the site'''
        time += self.__s1.get_time()

        if self.__s3 != 0:
            happening += str(self.time_converter(time))
            happening += "\nArrive at " + self.__s3.get_name() + ". \n"
            s3desc = self.__s3.get_desc()
            happening += s3desc
            happening += "\n\n"
            time += self.__s3.get_time()
            if self.__s4 != 0:
                happening += str(self.time_converter(time))
                happening += "\nArrive at " + self.__s4.get_name() + ". \n"
                s4desc = self.__s4.get_desc()
                happening += s4desc
                happening += "\n\n"
                time += self.__s4.get_time()
                if self.__s5 != 0:
                    happening += str(self.time_converter(time))
                    happening += "\nArrive at " + self.__s5.get_name() + ". \n"
                    s5desc = self.__s5.get_desc()
                    happening += s5desc
                    happening += "\n\n"
                    time += self.__s5.get_time()
                    if self.__s6 != 0:
                        happening += str(self.time_converter(time))
                        happening += "\nArrive at " + self.__s6.get_name() + ". \n"
                        s6desc = self.__s6.get_desc()
                        happening += s6desc
                        happening += "\n\n"
                        time += self.__s6.get_time()
                    else:
                        '''no site 6, no more time adjustments'''
                else:
                    '''no site 5, no more time adjustments'''
            else:
                '''no site 4, no more time adjustments'''
        else:
            '''no site 3, no more time adjustments'''
        return happening
    
class itinerary():
    def __init__(self, day1, day2, day3, day4):
        self.__d1 = day1
        self.__d2 = day2
        self.__d3 = day3
        self.__d4 = day4

    def printFullItinerary(self):
        str = "Day 1: "
        d1full = self.__d1.fullDayInformation()
        str += d1full
        if self.__d2 != 0:
            str += "\n\nDay 2: \n"
            d2full = self.__d2.fullDayInformation()
            str += d2full
            if self.__d3 != 0:
                str += "\n\nDay 3: \n"
                d3full = self.__d3.fullDayInformation()
                str += d3full
                if self.__d4 != 0:
                    str += "\n\nDay 4: \n"
                    d4full = self.__d4.fullDayInformation()
                    str += d4full
        else:
            '''Dont do anything, there's only one day'''
        return str


def generate_itinerary(site_list, daynum, howBusy, checkboxes):
    '''This function generates a random itinerary for the user.'''
    '''The values here are just placeholder values for the variables. in reality, these will be obtained from the survey. '''

    days = daynum
    busyness = howBusy
    checked = checkboxes
    my_sites = []
    
    for i in site_list:
        cat = i.get_category()
        if cat in checked:
            my_sites.append(i)

    if days == 1:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 7):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
        elif busyness == "moderate":
            for i in range (1, 5):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
        elif busyness == "light":
            for i in range (1, 3):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
        myItinerary = itinerary(d1, 0, 0, 0)
    elif days == 2:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 13):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
        elif busyness == "moderate":
            for i in range (1, 9):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
        elif busyness == "light":
            for i in range (1, 5):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, 0, 0)
    elif days == 3:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 19):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
            d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
        elif busyness == "moderate":
            for i in range (1, 13):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
            d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
        elif busyness == "light":
            for i in range (1, 7):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
            d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, d3, 0)
    elif days == 4:
        myPickedSites = []
        if busyness == "heavy":
            for i in range (1, 25):
                '''Six sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
            d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
            d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
            d4 = day(myPickedSites[18], myPickedSites[19], myPickedSites[20], myPickedSites[21], myPickedSites[22], myPickedSites[23])
        elif busyness == "moderate":
            for i in range (1, 17):
                '''Four sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
            d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
            d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
            d4 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], 0, 0)
        elif busyness == "light":
            for i in range (1, 9):
                '''Two sites in a day'''
                randselect = random.randint(1, len(my_sites)-1)
                myPickedSites.append(my_sites[randselect])
                my_sites.remove(my_sites[randselect])
            d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
            d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
            d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
            d4 = day(myPickedSites[6], myPickedSites[7], 0, 0, 0, 0)
        myItinerary = itinerary(d1, d2, d3, d4)
    return myItinerary


@bp.route('/makeNewItinerary', methods=['POST'])
def makeNewItinerary():
    if request.method == 'POST':
        city = request.form['city']
        checked = request.form.getlist('category')
        days = int(request.form['days'])
        busyness = request.form['busyness']

        '''berlin_sites = []
        empSite = site("Empty Site", "This Site is Empty", 100, 0, "No Address", "historical")
        num = 100 
        num2 = 0
        while num2 < num:
            berlin_sites.append(empSite)
            num2 += 1'''
        
        berlin_sites = []
        bbGate = site("Brandenburg Gate", "A historic landmark symbolizing peace and unity.", 25, 0, "Pariser Platz", "historical")
        berlin_sites.append(bbGate)
        eastSide = site("East Side Gallery", "The longest remaining section of the Berlin Wall, adorned with colorful murals.", 75, 0, "Mühlenstraße 79-81", "historical")
        berlin_sites.append(eastSide)
        reichstag = site("Reichstag Building", "The seat of the German Parliament, offering panoramic views of Berlin.", 200, 0, "Platz der Republik 1", "historical")
        berlin_sites.append(reichstag)
        wallMem = site("Berlin Wall Memorial", "A poignant reminder of the Cold War division of Berlin.", 150, 0, "Bernauer Straße 111", "historical")
        berlin_sites.append(wallMem)
        musIsl = site("Museum Island", "A UNESCO World Heritage Site housing five world-class museums.", 400, 5, "Museum Island", "historical")
        berlin_sites.append(musIsl)
        berCat = site("Berlin Cathedral", "A magnificent Baroque cathedral with stunning interior and exterior.", 100, 5, "Am Lustgarten 4", "historical")
        berlin_sites.append(berCat)
        charlie = site("Checkpoint Charlie", "A former border crossing point between East and West Berlin.", 25, 0, "Friedrichstraße 43-45", "historical")
        berlin_sites.append(charlie)
        tier = site("Tiergarten Park", "A vast urban park with diverse flora, fauna, and historical monuments.", 100, 0, "Tiergarten", "nature")
        berlin_sites.append(tier)
        tv = site("Berlin TV Tower", "A striking television tower offering panoramic views of the city.", 2, 15, "Potsdamer Platz 1", "family")
        berlin_sites.append(tv)
        char = site("Charlottenburg Palace", "A magnificent Baroque palace and gardens, once the residence of Prussian royalty.", 3, 10, "Spandauer Damm 10-22", "historical")
        berlin_sites.append(char)
        per = site("Pergamon Museum", "A world-renowned museum housing ancient artifacts from Greece, Rome, and the Middle East.", 3, 15, "Bodestraße 1-2", "family")
        berlin_sites.append(per)
        hum = site("Humboldt Forum", "A cultural complex dedicated to world cultures, history, and art.", 3, 10, "Unter den Linden 2", "historical")
        berlin_sites.append(hum)
        zoo = site("Berlin Zoo", "One of the oldest zoos in the world, home to a diverse range of animals.", 3, 15, "Hahnstraße 13", "family")
        berlin_sites.append(zoo)
        vik = site("Viktoriapark", "A picturesque hilltop park offering stunning views of the city.", 2, 0, "Kreuzbergstraße 70", "nature")
        berlin_sites.append(vik)
        hack = site("Hackescher Markt", "A vibrant district with historic courtyards, shops, and restaurants.", 2, 10, "Rosenthaler Straße 40-41", "family")
        berlin_sites.append(hack)
        bebl = site("Bebelplatz", "A historic square associated with the Nazi book burning of 1933.", 1, 0, "Bebelplatz", 'historical')
        berlin_sites.append(bebl)
        gede = site("Gedenkstätte Berliner Mauer", "A memorial site commemorating the victims of the Berlin Wall.", 2, 0, "Bernauer Straße 111", "historical")
        berlin_sites.append(gede)
        topo = site("Topographie des Terrors", "A historical site dedicated to the history of Nazi terror.", 2, 0, "Niederkirchnerstraße 8", "historical")
        berlin_sites.append(topo)
    

        krakow_sites = []
        newSite = site("Main Market Square", "The heart of Krakow's Old Town, surrounded by colorful buildings and historic churches.", 300, 5, "Rynek Główny 1", "historical")
        krakow_sites.append(newSite)
        newSite = site("Wawel Castle", "A majestic royal castle complex overlooking the Vistula River.", 300, 10, "ul. Wawel 5", "family")
        krakow_sites.append(newSite)
        newSite = site("St. Mary's Basilica", "A Gothic church famous for its distinctive trumpet call.", 200, 5, "Rynek Główny 1", "historical")
        krakow_sites.append(newSite)
        newSite = site("Kazimierz District", "The former Jewish quarter, now a vibrant cultural hub.", 300, 10, "ul. Miodowa 22", "historical")
        krakow_sites.append(newSite)
        newSite = site("Planty Park", "A green belt encircling the Old Town, perfect for leisurely walks.", 200, 0, "ul. Planty", "family")
        krakow_sites.append(newSite)
        newSite = site("Kraków Barbican", "A fortified gateway to the Old Town.", 100, 0, "ul. Basztowa 1", "historical")
        krakow_sites.append(newSite)
        newSite = site("Wieliczka Salt Mine", "A UNESCO World Heritage Site, a vast network of underground salt chambers.", 500, 30, "ul. Daniłowicza 20", "historical")
        krakow_sites.append(newSite)
        newSite = site("Rynek Główny Underground Museum", "A fascinating museum showcasing the history of Krakow's Main Market Square.", 200, 10, "Rynek Główny 1", "historical")
        krakow_sites.append(newSite)
        newSite = site("Czartoryski Museum", "A museum housing a diverse collection of art and historical artifacts.", 300, 10, "ul. św. Jana 19", "historical")
        krakow_sites.append(newSite)
        newSite = site("Collegium Maius", "The oldest building of the Jagiellonian University.", 200, 5, "ul. Gołębia 24", "historical")
        krakow_sites.append(newSite)
        newSite = site("National Museum in Krakow", "A comprehensive museum with a vast collection of art and artifacts.", 300, 10, "ul. św. Jana 22", "family")
        krakow_sites.append(newSite)
        newSite = site("Kraków Zoological Garden", "A zoo with a diverse range of animals, including many endangered species.", 300, 15, "ul. Krasińskiego 9a", "family")
        krakow_sites.append(newSite)
        newSite = site("Kopiec Kościuszki", "A hilltop mound commemorating Tadeusz Kościuszko, a Polish military leader.", 200, 0, "ul. Kościuszki 1", "nature")
        krakow_sites.append(newSite)
        newSite = site("Błonia Park", "A large park used for various events and festivals.", 200, 0, "Błonia", "nature")
        krakow_sites.append(newSite)
        newSite = site("Kraków Philharmonic Hall", "A beautiful concert hall hosting classical music performances.", 200, 10, "ul. Zwierzyniecka 1", "family")
        krakow_sites.append(newSite)
        newSite = site("St. Florian's Gate", "A historic gate leading to the Old Town.", 100, 0, "ul. Floriańska 41", "historical")
        krakow_sites.append(newSite)
        newSite = site("Kraków Main Railway Station", "A beautiful Art Nouveau railway station.", 100, 0, "pl. Jana Nowaka-Jeziorańskiego 1", "family")
        krakow_sites.append(newSite)
        newSite = site("Smoczy Smok Wawelski", "A mythical dragon sculpture near Wawel Castle.", 100, 0, "ul. Wawel 5", "family")
        krakow_sites.append(newSite)
        

        amsterdam_sites = []
        newSite = site("Rijksmuseum", "A world-class museum showcasing Dutch art and history.", 400, 20, "Museumstraat 1", "historical")
        amsterdam_sites.append(newSite)
        newSite = site("Anne Frank House", "A poignant museum dedicated to the life of Anne Frank.", 300, 15, "Prinsengracht 263-267", "historical")
        amsterdam_sites.append(newSite)
        newSite = site("Van Gogh Museum", "A museum dedicated to the life and work of Vincent van Gogh.", 300, 15, "Museumplein 6", 'historical')
        amsterdam_sites.append(newSite)
        newSite = site("Stedelijk Museum", "A museum of modern and contemporary art.", 300, 10, "Museumplein 10", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Vondelpark", "A large urban park with beautiful gardens, ponds, and playgrounds.", 200, 0, "Overtoom 185", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Dam Square", "A historic square in the heart of Amsterdam.", 200, 5, "Dam 1", 'historical')
        amsterdam_sites.append(newSite)
        newSite = site("Royal Palace", "A 17th-century palace on Dam Square.", 200, 10, "Dam 1", 'historical')
        amsterdam_sites.append(newSite)
        newSite = site("Nieuwe Kerk", "A medieval church on Dam Square.", 200, 5, "Dam 9", "family")
        amsterdam_sites.append(newSite)
        newSite = site("Jordaan District", "A charming neighborhood with canals, historic houses, and trendy shops.", 200, 5, "Jordaan", "historical")
        amsterdam_sites.append(newSite)
        newSite = site("Red Light District", "A historic district known for its red-lit windows.", 100, 5, "De Wallen", 'historical')
        amsterdam_sites.append(newSite)
        newSite = site("Hermitage Amsterdam", "A branch of the State Hermitage Museum in St. Petersburg.", 300, 15, "Amstel 51", 'historical')
        amsterdam_sites.append(newSite)
        newSite = site("NEMO Science Museum", "An interactive science museum for all ages.", 300, 10, "Oosterdok 2", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("A'DAM Lookout", "A panoramic observation deck on top of a former ferry terminal.", 200, 15, "Overhoeksplein 5", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Bloemenmarkt", "A floating flower market on the Singel canal.", 100, 5, "Singel", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Rembrandtplein", "A lively square with theaters, cinemas, and restaurants.", 200, 10, "Rembrandtplein", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Waterlooplein", "A vibrant market square with flea markets and vintage shops.", 200, 5, "Waterlooplein", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Begijnhof", "A historic cloister with charming houses and a peaceful atmosphere.", 100, 0, "Begijnhof", 'family')
        amsterdam_sites.append(newSite)
        newSite = site("Museumplein", "A square home to several world-class museums.", 200, 0, "Museumplein", 'historical')
        amsterdam_sites.append(newSite)
        newSite = site("Westerkerk", "A 17th-century church with a distinctive tower.", 100, 0, "Prinsengracht 297", 'historical')
        amsterdam_sites.append(newSite)
        if city == "berlin":
            createdItinerary = generate_itinerary(berlin_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        elif city == "krakow":
            createdItinerary = generate_itinerary(krakow_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        elif city == "amsterdam":
            createdItinerary = generate_itinerary(amsterdam_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        return render_template('itinerary.html', itin=itin)
    else:
        return render_template('survey.html')