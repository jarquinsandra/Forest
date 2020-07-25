"""

AUTOR: jarquinsandra


"""
"""

AUTOR: jarquinsandra


"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    SECRET_KEY = '5e04a4955d8878191923e86fe6a0dfb24edb226c87d6c7787f35ba4698afc86e95cae409aebd47f7'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://jarquinsandra:plasma86@jarquinsandra.mysql.pythonanywhere-services.com/jarquinsandra$Forest"
    #SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    #username="jarquinsandra",
    #password="plasma86",
    #hostname="jarquinsandra.mysql.pythonanywhere-services.com",
    #databasename="'jarquinsandra$Forest'",
     #   )
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    #Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db)
     #Import Blueprints

    from .consensus import db_manager
    app.register_blueprint(db_manager)


    register_error_handlers(app)

    return app

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

class TempSpectra(db.Model):
	__tablename__= 'temp_spectra'
	id = db.Column(db.Integer, primary_key = True)
	mz = db.Column(db.Float, unique=False, nullable=False)
	int_rel = db.Column(db.Float, unique=False, nullable=False)


class TempSpectra2(db.Model):
	__tablename__= 'temp_all_spectra'
	id = db.Column(db.Integer, primary_key = True)
	mz = db.Column(db.Float, unique=False, nullable=False)
	intensity = db.Column(db.Float, unique=False, nullable=False)

