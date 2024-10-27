from flask import render_template

class SurveyController:

    def index():
        data = {}
 

        return render_template('survey.html', data=data)
      