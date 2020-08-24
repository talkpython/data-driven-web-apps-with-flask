import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)

def register_blueprints():
    from pypi_org.views import home_views


if __name__ == '__main__':
    main()