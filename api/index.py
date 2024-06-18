from flask import Flask, request  # Ensure these imports are present

app = Flask(__name__)  # Initialize your Flask application

@app.route('/')
def index():
    return form()

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
    try:
        x = request.form['x']
        y = request.form['y']
        result = int(x) + int(y)  # This might raise ValueError if x or y are not integers
        return str(result)
    except ValueError:
        return "Please enter valid numbers."

if __name__ == "__main__":
    app.run(debug=True)  # Running the app with debug=True can provide more detailed error messages