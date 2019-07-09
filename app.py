from flask import Flask


app = Flask(__name__)


# Testing URL
@app.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

app.run(host='0.0.0.0', port=8081, debug=True)
