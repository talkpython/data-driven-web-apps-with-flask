import os
import sys

import flask
from flask_session import Session

from pypi_org.configs import app_config

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
import pypi_org.data.db_session as db_session

app = flask.Flask(__name__)
app.config.from_object(app_config)


def main():
    configure()
    app.run(debug=True, port=5006, host='localhost')


def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")

    setup_db()
    print("DB setup completed.")

    setup_session_server()
    print("", flush=True)


def setup_session_server():
    Session(app)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite')

    db_session.global_init(db_file)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views
    from pypi_org.views import account_views
    from pypi_org.views import seo_view

    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(seo_view.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()
