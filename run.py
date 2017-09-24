import flask
from flask import Flask, render_template, redirect, abort, url_for, session, flash
from flask_bootstrap import Bootstrap
from formS import NameForm #Import NameForm from formS.py chech the file
# from flash import msgTest
"""
Flask-Bootstrap is imported from the flask.ext name-space and initialized by
passing the application instance in the constructor
"""

app = Flask(__name__, static_folder='public/assets', template_folder='templates')
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

#========================= FIRST STEP - START FLASK =========================#

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

#========================= SECOND STEP  - WEB FORMS =========================#

# OLD VERSION TO FORM.NAME.DATA - TEST THIS VERSION FIRST 
# @app.route('/forms', methods=['GET', 'POST']) #example to use the methods GET and POST
# def formsIndex():
# 	name = None
# 	form = NameForm()
# 	if form.validate_on_submit():
# 		name = form.name.data
# 		form.name.data = ''
# 	return render_template('newindex.html', form=form, name=name)


#NEW VERSION TO FORM.NAME.DATA
@app.route('/forms2',  methods=['GET', 'POST']) #Test new function for form
def newform():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
	return render_template('newindex.html', form=form, name=session.get('name'))

@app.route('/msg', methods=['GET', 'POST']) #New function to try flash message
def msgTest():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('You have changed your name!')
		session['name'] = form.name.data
		form.name.data = ''
	return render_template('newindex.html', form = form, name= session.get('name'))

#========================= THIRD STEP  - SQL DATABASE =========================#


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4000)
