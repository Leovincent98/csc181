from flask import Flask, render_template, request
from models import *
import os






@app.route('/',methods=['GET', 'POST'])
def index():
	coords = Landmarks.query.all()
	return render_template("home.html",coords = coords, msg="hello")

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
def map():
	return render_template("map.html")

@app.route('/landmark/<id>',methods=['GET'])
def landmark(id):
	land = Landmarks.query.filter_by(land_id=id).first()
	college = land.name
	return render_template("landmark.html", college=college)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'C:\Users\Admin\Desktop\upload\static')
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