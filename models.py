import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://postgres:imapkuno@localhost/map1"
app.config['SECRET_KEY'] = 'veryhard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_SESSION_FOR_NEXT'] = True
app.secret_key = os.urandom(24)
app.debug = True
db = SQLAlchemy(app)

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)



class Landmarks(db.Model):
	land_id =  db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	points = db.Column(db.String(200), unique=True)
	type_ = db.Column(db.String(100))

	def __init__(self, name, points, type_):
		self.name = name
		self.points = points
		self.type_ = type_



class Rooms(db.Model):
	room_id = db.Column(db.Integer, primary_key = True)
	floor_id = db.Column(db.Integer, db.ForeignKey('floors.floor_id'))
	room_num = db.Column(db.String(10), unique = True)


	def __init__(self, floor_id, room_num):
		self.floor_num = floor_num
		self.room_num = room_num

class Floors(db.Model):
	floor_id = db.Column(db.Integer, primary_key = True)
	floor_landmark = db.Column(db.String(10), unique = True)
	rf_id = db.relationship("Rooms", uselist =False, backref = "floor_room")


	def __init__(self, floor_num, room_num):
		self.floor_num = floor_num
		self.room_num = room_num

class Roommarks(db.Model):
	room_id =  db.Column(db.Integer, primary_key=True)
	room_name = db.Column(db.String(50), unique=True)
	points = db.Column(db.String(200), unique=True)
	floor_num= db.Column(db.String(100))

	def __init__(self, room_name, points, floor_num):
		self.room_name = room_name
		self.points = points
		self.floor_num = floor_num

db.create_all()
