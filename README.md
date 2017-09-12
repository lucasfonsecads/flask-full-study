    Flask Full Study

Here we'll use all resources off flask with start one simple application's - 'Hello World' to a full api project.

- [x] 'Hello Word'
- [x] Render template
- [x] Redirect

    
    
## Flask Full Study
    
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
