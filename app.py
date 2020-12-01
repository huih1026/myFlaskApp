import sys
from flask import Flask
# create an app by flask
app = Flask(__name__)
# given the route to let the broswer to find
@app.route("/")

def index():
	return "hello,world"
