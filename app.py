from flask import Flask
from framework.Database import Database
from framework.Router import Router
import config

#Start the app..
app = Flask(__name__, static_url_path='/static', 
                    static_folder=config.STATIC_DIR,
                    template_folder=config.VIEWS_DIR)


#Confing start...
app.config.from_object(config)

#Database connection
Database = Database(app)

Router.run(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
