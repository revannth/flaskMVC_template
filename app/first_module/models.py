#models.py

#Import your database object that was initialised in init of the apps.py file
from app import db

#Define a base model(which would be used by everyone) like so:
class Base(db.Model):
	#Your content goes here

#Define a User model like so:
class User(Base):

	#Your content goes here and depends on what kind of application is being developed