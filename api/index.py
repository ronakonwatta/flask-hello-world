from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/html')
def api():
    return '''
<h1>HTML</h1>

'''

@app.route('/form')
def form():
    return '''
<form action="/cal" method="post">
  <input type="text" name="x">
  <input type="text" name="y">
  <input type="submit" value="Submit">
</form>
'''

@app.route('/cal', methods=['POST'])
def cal():
    x = request.form['x']
    y = request.form['y']
    return str(int(x) + int(y))