
class Router:

    def run(app):
        
        print("Web server starting")
        
        from . import Auth
        app.register_blueprint(Auth.bp)

        #Home Page
        from application.routes.HomeRouter import HomeRouter
        app.register_blueprint(HomeRouter, url_prefix="/")

        #How It Works Page
        from application.routes.HowRouter import HowRouter
        app.register_blueprint(HowRouter, url_prefix="/howitworks")