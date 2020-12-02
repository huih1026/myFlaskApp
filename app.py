from flask import Flask, render_template

# create an app by flask
app = Flask(__name__)

# given the route to let the broswer to find
@app.route("/")

def index():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)