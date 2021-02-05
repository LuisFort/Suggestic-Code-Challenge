"""
In this file you will find the libraries  configuration for the app
"""

from flask import Flask ,request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import datetime
import os

#loading database credentials

load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
passwd = os.getenv('DB_PASS')
database = os.getenv('DB_NAME')

# initializing the app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ user + ':' + passwd + '@' + host + '/' + database 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# extensions

db = SQLAlchemy(app)
CORS(app)