"""
In this file you will find the code to run de app.
The app is imported from routes because 
the endpoint was defined there.
"""
#Importing
from config import os, db
from routes import app

if __name__ == '__main__':
	#In this piece of code the tables are created if they don´t exist
	#in the database
	if not os.path.exists('db.sqlite'):
		db.create_all()
	#Here the debug mode is turned off,
	#the port is defined, and the app is run
	app.run(host= '0.0.0.0', debug = False, port = 8080)