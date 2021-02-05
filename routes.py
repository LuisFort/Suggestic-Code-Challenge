"""
In this file you will find the routes for the endpoints
"""
#Importing some variables from config file
from config import (os, jsonify, request, app)

#Importing the file where the functions are
from Controllers import dataController

#Defining the url and the method for the endpoint 
@app.route('/flatten', methods=['POST'])
def function():

	"""
	Thisfunction will receive the nested sequence.
	First it will validate that the input data has the sequence,
	in the case that the array doesn't exist it returns an error.

	If the the array exists, the function will be called to flatten it.
	
	Once the array has been flattened, the function is called to save
	it in the database
	"""
	inputData = request.get_json(silent=True)
	print(inputData)
	
	try :
		originArray = inputData['items']
	except :
		return jsonify({"status": "failed", "msg": 'Missing arguments'}),400

	try :
		flattenArray = dataController.flatten(originArray)
		isSaved = dataController.saveArray(flattenArray)
		if isSaved:
			return jsonify({"status": "success", "msg": "The array was saved in database", "flattenArray": flattenArray}), 200
		else:
			return jsonify({"status": "success", "msg": "The array was not saved in database","flattenArray": flattenArray}), 200
	except Exception as error:
		print(error)
		return jsonify({'status': 'failed', 'msg': 'Something bad happened'}), 500	


@app.route('/onlyFlatten', methods=['POST'])
def onlyFlatten():

	"""
	This endpoint was created only to verify the flatten
	
	This function will receive the nested sequence.
	First it will validate that the input data has the sequence,
	in the case that the array doesn't exist it returns an error.

	If the the array exists, the function will be called to flatten it.
	
	"""
	inputData = request.get_json(silent=True)
	print(inputData)
	
	try :
		originArray = inputData['items']
	except :
		return jsonify({"status": "failed", "msg": 'Missing arguments'}),400

	try :
		flattenArray = dataController.flatten(originArray)	
		return jsonify({"status": "success","flattenArray": flattenArray}), 200
	except Exception as error:
		print(error)
		return jsonify({'status': 'failed', 'msg': 'Something bad happened'}), 500