from flask import render_template

class HowController:

    def index():
        data = {}

        return render_template('howitworks.html', data=data)
      