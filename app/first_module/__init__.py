#__init__.py

#Import flask and template operations
from flask import Flask,render_template

#Import Database
from flask.ext.sqlalchemy import SQLAlchemy

#Define the WSGI application object

app = Flask(__name__)

#Import all the configuration objects
app.config.from_object('config')

#Create the database object

db = SQLAlchemy(app)

from app.first_module.controllers import first_module as first

app.register_blueprint(first)

db.create_all()
