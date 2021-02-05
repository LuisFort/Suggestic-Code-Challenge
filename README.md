# Suggestic-Code-Challenge
In this repository you will find the code for the Suggestic Code Callenge. In this project I raised a web service to flatten a nested sequence into a single
list of values. Once the sequence was flattened, I save the result in a SQL database before sending the response.

# How to install
Clone de repo with the following command:

git clone https://github.com/LuisFort/Suggestic-Code-Challenge.git

**This project runs in Python3.**

I suggest installing a virtual environment with Python3 and run the project within it. 
You can see how to install a virtual enviroment in the link below.

https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b

# How to use

First you must install the dependencies to run the project, run the following command in the terminal:

pip3 install -r requirements.txt

**Now you must create your own .env file, without it you will get an error when you're trying to run the app.**

The .env file must be in the same folder and it must have the following information:

- DB_HOST=127.0.0.1
- DB_USER=User
- DB_PASS=Password
- DB_NAME=DataBase

This information is to connect with your local Database. **Change the information for your own credentials**.

**In this project I use MYSQL**, so you must have SQL installed on your computer. If you don´t have SQL you must install it, otherwise you will not be able to run the project

Once you have done the steps above, you only have to run the "run.py" file with the following command:

python3 run.py

After that, you will see that the service is already (on your localhost in the port 8080).

In this project I made two endpoints, ones to only test the flattening, and the other to test the flattening en save the result in the database.

To test the service you can use Postman (I used it), if you want to save the result in the database you have to use "/flatten", and if you only want to see the result you have to use "/onlyFlatten".





