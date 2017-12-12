#controller.py


#Import flask dependencies

from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

#Import password/encryption tools
from werkzeug import check_password_hash, generate_password_hash


#Import the database object
from app import db

#Import the necessary class modules from model

from app.first_module.models import User
