from flask import Flask, render_template, request, url_for, flash, redirect
from sqlalchemy.orm import sessionmaker
from forms import LoginForm
from models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryhard'

@app.route('/',methods=['GET'])
def index():
	coords = Landmarks.query.all()
	return render_template("index.html",coords = coords, msg="hello")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@mail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)	

@app.route('/setpoints',methods=['GET' , 'POST'])
def setpoints():
	coords = Landmarks.query.all()
	if request.method == "POST":
		namex  = request.form['name']
		pointsx = request.form['points']
		type_x = request.form['type']
		
		land = Landmarks(name = namex, points=str(pointsx), type_=type_x)
		db.session.add(land)
		db.session.commit()
		coords = Landmarks.query.all()
		return render_template('index.html',coords = coords, msg="hello")
	
	return render_template('setpoints.html')

@app.route('/map',methods=['GET'])
def map():
	return render_template("setpoints.html")

@app.route('/landmark/<id>',methods=['GET'])
def landmark(id):
	land = Landmarks.query.filter_by(land_id=id).first()

	return render_template("landmark.html", land=land)

	
if __name__ == '__main__':
	app.run(debug=True)