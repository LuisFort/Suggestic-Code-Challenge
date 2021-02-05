"""
In this file you will find the way to define de table model
to save the data
"""
from config import db, datetime

class FlattenArray(db.Model):
	"""
	Here the table name is defined, the id field is created as
	primary key, the array field es created to save de flatten array
	and the created at field and updated_at filed are created 
	"""
	__tablename__ = 'flatten_array'
	id = db.Column(db.Integer, primary_key=True)
	array = db.Column(db.String(500))
	created_at = db.Column(db.DateTime(), default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now(), default=datetime.datetime.now())