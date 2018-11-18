from map import app
import os

if __name__=='main':
	#app.run()
	port = int(os.environ.grt("PORT",5000))
	app.run(host-'0.0.0.0',port=port)