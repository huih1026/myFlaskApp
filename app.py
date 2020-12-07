from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data  import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt

# create an app by flask
app = Flask(__name__)

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lxx1217#'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSOR'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)


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


# define forms, use class to store combined data set
# this class wrap or cast the incoming para Form by using the library function
class RegisterForm(Form):
	name 	 = StringField('Name', [validators.Length(min=1, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)]) 
	email 	 = StringField('Email', [validators.Length(min=6, max=50)])

	# DataRequired(): must from wtforms.validators import DataRequired
	password = PasswordField('Password', [
		DataRequired(),
		validators.EqualTo('confirm', message='Passwords Not Match')])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))

		# create cursor
		cur = mysql.connection.cursor()

		cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

		# commit to DB
		mysql.connection.commit()

		# close connection
		cur.close()

		flash('You are now regiseterd and can log in', 'success')

		redirect(url_for('index'))

	return render_template('home.html', form=form)


if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(debug=True)