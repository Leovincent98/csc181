from flask import Flask, render_template, request, url_for, flash, redirect
from forms import LoginForm
from models import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veryhard'

@app.route('/',methods=['GET', 'POST'])
def index():
	coords = Landmarks.query.all()
	return render_template("home.html",coords = coords, msg="hello")

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
		return render_template('home.html',coords = coords, msg="hello")
	
	return render_template('setpoints.html')



@app.route('/activateUpdateMap', methods=['GET'])
def activateUpdateMap():
	os.system('python updateFloors.py')

@app.route('/upload', methods=['GET'])
def activate():
	return render_template("upload.html")

@app.route('/map',methods=['GET'])
def home():
	return render_template("home.html")

@app.route('/landmark/<id>',methods=['GET'])
def landmark(id):
	land = Landmarks.query.filter_by(land_id=id).first()
	return render_template("landmark.html", land=land)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'C:\Users\kaju\Desktop\csc181\static')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
  
    return render_template("complete.html")

@app.route("/update", methods=['GET'])
def update():
    return render_template("upload.html")




if __name__ == '__main__':
	app.run(debug=True)