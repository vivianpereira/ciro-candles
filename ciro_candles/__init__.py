# import flask - from the package import a module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(
        __name__
    )  # this is the name of the module/package that is calling this app
    app.debug = True

    # set the app configuration data
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///ciro_candles.sqlite'

    # initialize db with flask app
    db.init_app(app)

    # add the Blueprint
    from . import views

    app.register_blueprint(views.bp)

    return app
