from flask import render_template

class ItineraryController:

    def index():
        data = {}
 

        return render_template('itinerary.html', data=data)
      