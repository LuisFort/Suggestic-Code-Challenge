"""
In this field you will find the functions to flatten the array and
save the flatten array
"""
from config import db, datetime
from models import FlattenArray

def flatten(nestedArray):
	"""
	I lopp through the fisrt list checking the type of each element,
	if it's another list I call the function again, so it only loops
	through each element of the nested lists once.

	"""
	flattenArray = []
	for element in nestedArray :
		if type(element) is list:
			flattenArray += flatten(element)
		else :
			flattenArray.append(element)

	return flattenArray

def saveArray(array):
	"""
	I convert the array in a string to be saved in one
	field in the database. If something wrong happened when
	saving the array a False is return to indicate that the array
	was not saved.
	"""

	try :
		array = ','.join([str(num) for num in array])
		data = FlattenArray(array=array, created_at = datetime.datetime.now(), updated_at = datetime.datetime.now())
		db.session.add(data)
		db.session.commit()
		return True
	except Exception as error:
		print(error)
		return False