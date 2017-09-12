import flask
from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder='public/assets') #Here we found the unique requered argument to the Flask -> (__name__)
#Here can you see the static_folder is one way to determine your public folder to access


@app.route('/') #Hello World for everybody, run you app and show for the world 
def index():
	return '<h1>Hello World</h1>'

@app.route('/template')
def renderT():
	return render_template('index.html') #use to render the template with jinja2

@app.route('/user/<name>')
def userL(name):
	return render_template('user.html', name=name)

@app.route('/redirect') #example to use redirect with flask 
def redirect():
	return redirect('https://github.com')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4000)