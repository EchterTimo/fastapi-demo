from flask import Flask
import config

app = Flask(__name__)


@app.route('/')
def root():
    return {
        "code": 200,
        "message": "it works"
    }


if __name__ == '__main__':
    app.run(
        host=config.host,
        port=config.port,
        debug=config.debug,
    )
