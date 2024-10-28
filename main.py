from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return "it works"


@app.route('/json')
def json_endpoint():
    return {
        "code": 200,
        "message": "it works"
    }
