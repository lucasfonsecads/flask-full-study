import flask
from flask import Flask, render_template, redirect, abort
from flask_bootstrap import Bootstrap 
"""
Flask-Bootstrap is imported from the flask.ext name-space and initialized by
passing the application instance in the constructor
"""

app = Flask(__name__, static_folder='public/assets') 
"""
Here we found the unique requered argument to the Flask -> (__name__)
Here can you see the static_folder is one way to determine your public folder to access
"""
app.config['SECRET_KEY'] = 'my-precious' 
"""
Choice one hard string for protect your webapp
if you like use python in command line generate your key. For this go in README and see the example
"""
bootstrap = Bootstrap(app) #Here we start the bootstrap application using the app 

@app.route('/') #Hello World for everybody, run you app and show for the world 
def index():
	return '<h1>Hello World</h1>'

@app.route('/template')
def renderT():
	return render_template('index.html') #use to render the template with jinja2

@app.route('/user/<name>') 
#Example to use variable in your template with dynamic route.
#For access go in localhost/user/your-name 
def user(name):
	return render_template('user.html', name=name)

@app.route('/bootstrap/<name>')
#Example to access your bootstrap template with you put localhost/boostrap/your-name 
#you will see the magic of flask
def teste(name):
	return render_template('base.html', name=name)

@app.route('/redirect') #example to use redirect with flask 
def redirect():
	return redirect('https://github.com')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4000)