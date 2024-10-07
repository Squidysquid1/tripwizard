
class Router:

    def run(app):
        
        print("Web server starting")
        
        #Index Page!
        from application.routes.HomeRouter import HomeRouter
        app.register_blueprint(HomeRouter, url_prefix="/")