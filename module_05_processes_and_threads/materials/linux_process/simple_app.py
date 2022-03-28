import flask

from flask import current_app


app = flask.Flask(__name__)

@app.endpoint('/test')
def test_endpoint():
    print("hello")
    return 'Test endpoint was called!'


if __name__ == '__main__':
    app.run()
