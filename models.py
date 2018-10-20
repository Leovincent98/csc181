import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from flask_sqlalchemy import SQLAlchemy
# from flask_login import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://postgres:postgres@localhost/map"
app.config['SECRET_KEY'] = 'veryhard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_SESSION_FOR_NEXT'] = True
app.secret_key = os.urandom(24)
app.debug = True
db = SQLAlchemy(app)


class Landmarks(db.Model):
	land_id =  db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	points = db.Column(db.String(200), unique=True)
	type_ = db.Column(db.String(100))

	def __init__(self, name, points, type_):
		self.name = name
		self.points = points
		self.type_ = type_

db.create_all()
