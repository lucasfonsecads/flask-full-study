
## Flask Full Study

Here we'll abordding all recurses of flask with start one simple appication's - 'Hello World' to a full api prroject.

- [x] 'Hello Word'
- [x] Render template
- [x] Redirect
- [x] Static Folder
- [x] Meeting Jinja2
- [x] Meeting bootstrap
- [ ] Web Forms


 - First Step start one virtualenv with this command:

 ```shell
 virtualenv env
 cd env
 source bin/activate
 ```
 - Requirements

 ```shell
 pip install flask
 ```

 - Determine your public folder:
 ```python
 app = Flask(__name__, static_folder='public/assets')
 #one example to access the folder public and assets before
 ```

 - Example to create one app flask:

```python
import flask
from flask import Flask

app = Flask(__name__)

```

- Example to access one route and use Jinja2 to render:

```python
@app.route('/')
def index():
  return '<h1>Hello World</h1>
```

- Example to render one template wiht Jinja2:

```python
@app.route('/template')
def renderT():
  return render_template('index.html')
#remember to import render_template from flask
```
- Example do redirect one access:

```python
@app.route('/redirect')
def redirecT():
  return redirect('https://github.com/lucasfonmiranda')
#remeber to import redirect from flask

```

- Example to determine web server:

```python
if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 4000)
```

- For run your app:
```shell
python run.py
```

## Jinja2 Section

- Jinja2 offers several control structures can be used to alter the flow od the template.

- The following example shows how conditional statements can be entered in a template:

```html
{% if user %}
  Hello, {{ user }}!
{% else %}
  Hello stranger!
{% endif %}
```

- Another common need in templates is to render a list of elements:

```html
<ul>
  {% for comment in comments %}
  <li>{{ comment }}</li>
  {% endfor %}
</ul>
```

## Using bootstrap framework from Twitter with flask:

- Requirements:

```shell
pip install flask-bootstrap
```

- Import Bootstrap for your flask application:

```python
from flask_bootstrap import Bootstrap

boostrap = Boostrap(app)
```
For see one page using bootstrap go in templates/base.html
run your app and access localhost/bootstrap and see the magic...

## Web Forms

- Requirements:

```shell
pip install flask-wtf
```

- Cross-Site Request Forgery(CSRF) Protection:

A CSRF attack occurs when a malicious website sends requests to a different website on which the victim is logged in. By default, Flask-WTF protects all forms against CSRF attacks.

- To implement CSRF proteciton:

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard string'
```

- For generate one key in python command line:
```python
from os import urandom
from base64 import b64encode
import os

random = os.urandom(64)
key = b64encode(random).decode('utf-8')
print (key)
```
- First function use Web Forms:

```python
@app.route('/forms', methods=['GET', 'POST']) #example to use the methods GET and POST
def formsIndex():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('newindex.html', form=form, name=name)
```
