"""

AUTOR: jarquinsandra


"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_module):
    app = Flask(__name__)
    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
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



