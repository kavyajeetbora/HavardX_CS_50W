from flask import Flask

## How does the flask know which application to run when
## command flask run in entered in the terminal??

## Answer: in flask by default relies on environment variable
## which is a variable that is set inside of the terminal
## variable = the source file of the application
## by default the source file is app.py

## we can also manually setup the enviromnent variable
## by entering the following code in terminal:
## export FLASK_APP=application.py

app = Flask(__name__)

@app.route("/")
def index():
 return "Hello, world"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
