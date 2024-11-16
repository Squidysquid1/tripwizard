
class Router:

    def run(app):
        
        print("Web server starting")
        
        from . import Auth
        app.register_blueprint(Auth.bp)

        #Home Page
        from application.routes.HomeRouter import HomeRouter
        app.register_blueprint(HomeRouter, url_prefix="/home")

        #How It Works Page
        from application.routes.HowRouter import HowRouter
        app.register_blueprint(HowRouter, url_prefix="/howitworks")

        #Survey Page
        from application.routes.SurveyRouter import SurveyRouter
        app.register_blueprint(SurveyRouter, url_prefix="/survey")


        #Itinerary Page
        from application.routes.ItineraryRouter import ItineraryRouter
        app.register_blueprint(ItineraryRouter, url_prefix="/")