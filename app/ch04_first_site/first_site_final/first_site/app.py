import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

app.run()
