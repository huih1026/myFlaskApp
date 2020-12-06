from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data  import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

# create an app by flask
app = Flask(__name__)


Articles = Articles()


# given the route to let the broswer to find
@app.route('/')
def index():
	return render_template('home.html')

# "/about is given as the route when click navbar icon, 
# here says if detect this /about, then render the about.html file in template
@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/articles')
def articles():
	return render_template("articles.html", articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
	return render_template("article.html", id=id)

if __name__ == '__main__':
	app.run(debug=True)