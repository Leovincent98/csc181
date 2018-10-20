from flask import Flask, render_template
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
	
	return render_template('setpoint.html')

@app.route('/map',methods=['GET'])
def map():
	return render_template("setpoint.html")

@app.route('/coet',methods=['GET'])
def coet():
	return render_template("coet.html")

@app.route('/ced',methods=['GET'])
def ced():
	return render_template("ced.html")

@app.route('/coet_con',methods=['GET'])
def coet_con():
	return render_template("coet_con.html")

@app.route('/cbaa',methods=['GET'])
def cbaa():
	return render_template("cbaa.html")

@app.route('/csm',methods=['GET'])
def csm():
	return render_template("csm.html")

@app.route('/gym',methods=['GET'])
def gym():
	return render_template("gym.html")

@app.route('/scs',methods=['GET'])
def scs():
	return render_template("scs.html")

@app.route('/ids',methods=['GET'])
def ids():
	return render_template("ids.html")

@app.route('/lawn',methods=['GET'])
def lawn():
	return render_template("lawn.html")

@app.route('/admin',methods=['GET'])
def admin():
	return render_template("admin.html")

@app.route('/cass',methods=['GET'])
def cass():
	return render_template("cass.html")

@app.route('/cbaa_extension',methods=['GET'])
def cbaa_extension():
	return render_template("cbaa_extension.html")

@app.route('/clinic',methods=['GET'])
def clinic():
	return render_template("clinic.html")

if __name__ == '__main__':
	app.run(debug=True)