from flask import Flask, render_template, request
from models import *





@app.route('/',methods=['GET'])
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

@app.route('/map',methods=['GET'])
def map():
	return render_template("setpoints.html")

@app.route('/landmark/<id>',methods=['GET'])
def landmark(id):
	land = Landmarks.query.filter_by(land_id=id).first()
	college = land.name
	return render_template("landmark.html", college=college)




if __name__ == '__main__':
	app.run(debug=True)