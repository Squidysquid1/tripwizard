from flask import Flask, request, render_template
import random

app = Flask(__name__)

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
        time = 850
        happening = str(self.time_converter(time))
        happening += "\t\t"
        happening += "Leave Hotel and go to " + self.__s1.get_name() + ". \n"
        time += 50
        
        '''happening = "\nArrive at " + self.__s1.get_name() + ". \n"
        siteOneTime = self.__s1.get_time()
        time += siteOneTime
        self.time_converter(time)'''

        happening += str(self.time_converter(time))
        happening += "\nArrive at " + self.__s1.get_name() + ". \n"
        happening += self.__s1.get_desc
        happening += "\n\n"
        time += self.__s1.get_time()

        happening += str(self.time_converter(time))
        happening += "\nArrive at " + self.__s2.get_name() + ". \n"
        happening += self.__s2.get_desc
        happening += "\n\n"
        time += self.__s2.get_time() 

        if self.__s3 != 0:
            happening += str(self.time_converter(time))
            happening += "\nArrive at " + self.__s3.get_name() + ". \n"
            happening += self.__s3.get_desc
            happening += "\n\n"
            time += self.__s3.get_time()
            if self.__s4 != 0:
                happening += str(self.time_converter(time))
                happening += "\nArrive at " + self.__s4.get_name() + ". \n"
                happening += self.__s4.get_desc
                happening += "\n\n"
                time += self.__s4.get_time()
                if self.__s5 != 0:
                    happening += str(self.time_converter(time))
                    happening += "\nArrive at " + self.__s5.get_name() + ". \n"
                    happening += self.__s5.get_desc
                    happening += "\n\n"
                    time += self.__s5.get_time()
                    if self.__s6 != 0:
                        happening += str(self.time_converter(time))
                        happening += "\nArrive at " + self.__s6.get_name() + ". \n"
                        happening += self.__s6.get_desc
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
        str = "Day 1: \n"
        str += self.__d1.fullDayInformation()
        if self.__d2 != 0:
            str += "\n\nDay 2: \n"
            str += self.__d2.fullDayInformation()
            if self.__d3 != 0:
                str += "\n\nDay 3: \n"
                str += self.__d3.fullDayInformation()
                if self.__d4 != 0:
                    str += "\n\nDay 4: \n"
                    str += self.__d4.fullDayInformation()
        else:
            '''Dont do anything, there's only one day'''
        return str

berlin_sites = []
empSite = site("Empty Site", "This Site is Empty", 100, 0, "No Address", "historical")
num = 100 
num2 = 0
while num2 < num:
    berlin_sites.append(empSite)
    num += 1

@app.route('/', methods=['POST'])
def makeNewItinerary():
    if request.method == 'POST':
        city = request.form['city']
        checked = request.form.getlist('checkbox')
        days = int(request.form['days'])
        busyness = request.form['busyness']

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

        
            '''This is where the itinerary is generated.'''

            totsites = len(my_sites)

            if days == 1:
                myPickedSites = []
                if busyness == "heavy":
                    for i in range (1, 7):
                        '''Six sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
                elif busyness == "moderate":
                    for i in range (1, 5):
                        '''Four sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
                elif busyness == "light":
                    for i in range (1, 3):
                        '''Two sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
                myItinerary = itinerary(d1, 0, 0, 0)
            elif days == 2:
                myPickedSites = []
                if busyness == "heavy":
                    for i in range (1, 13):
                        '''Six sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
                    d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
                elif busyness == "moderate":
                    for i in range (1, 9):
                        '''Four sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
                    d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
                elif busyness == "light":
                    for i in range (1, 5):
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
                    for i in range (1, 19):
                        '''Six sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
                    d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
                    d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
                elif busyness == "moderate":
                    for i in range (1, 13):
                        '''Four sites in a day'''
                        totsites = totsites - 1
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
                    d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
                    d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
                elif busyness == "light":
                    for i in range (1, 7):
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
                    for i in range (1, 25):
                        '''Six sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], myPickedSites[4], myPickedSites[5])
                    d2 = day(myPickedSites[6], myPickedSites[7], myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11])
                    d3 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], myPickedSites[16], myPickedSites[17])
                    d4 = day(myPickedSites[18], myPickedSites[19], myPickedSites[20], myPickedSites[21], myPickedSites[22], myPickedSites[23])
                elif busyness == "moderate":
                    for i in range (1, 17):
                        '''Four sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], myPickedSites[2], myPickedSites[3], 0, 0)
                    d2 = day(myPickedSites[4], myPickedSites[5], myPickedSites[6], myPickedSites[7], 0, 0)
                    d3 = day(myPickedSites[8], myPickedSites[9], myPickedSites[10], myPickedSites[11], 0, 0)
                    d4 = day(myPickedSites[12], myPickedSites[13], myPickedSites[14], myPickedSites[15], 0, 0)
                elif busyness == "light":
                    for i in range (1, 9):
                        '''Two sites in a day'''
                        randselect = random.randint(1, totsites)
                        myPickedSites.append(my_sites[randselect])
                        my_sites.remove(my_sites[randselect])
                    d1 = day(myPickedSites[0], myPickedSites[1], 0, 0, 0, 0)
                    d2 = day(myPickedSites[2], myPickedSites[3], 0, 0, 0, 0)
                    d3 = day(myPickedSites[4], myPickedSites[5], 0, 0, 0, 0)
                    d4 = day(myPickedSites[6], myPickedSites[7], 0, 0, 0, 0)
                myItinerary = itinerary(d1, d2, d3, d4)
                return myItinerary

        if city == "berlin":
            createdItinerary = generate_itinerary(berlin_sites, days, busyness, checked)
            itin = createdItinerary.printFullItinerary()

        itin = createdItinerary.printFullItinerary()
        return render_template('itinerary.html', itin=itin)
    else:
        return render_template('survey.html')



if __name__ == '__main__':
    app.run(debug=True)
