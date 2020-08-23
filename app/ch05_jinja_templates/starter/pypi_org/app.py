import flask

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlachemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'},
    ]

@app.route("/")
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages=test_packages)

@app.route("/about")
def about():
    return flask.render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)