
class Router:

    def run(app):
        
        print("Web server starting")
        
        from . import Auth
        app.create_acc_blueprint(Auth.bp)

        #Index Page!
        from application.routes.HomeRouter import HomeRouter
        app.create_acc_blueprint(HomeRouter, url_prefix="/")