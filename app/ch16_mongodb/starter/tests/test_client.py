# noinspection PyPackageRequirements
import pytest

import sys
import os

container_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, container_folder)

import pypi_org.app  # noqa 402
from pypi_org.app import app as flask_app  # noqa 402


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    client = flask_app.test_client()

    # noinspection PyBroadException,PyUnusedLocal
    try:
        pypi_org.app.register_blueprints()
    except Exception as x:
        # print(x)
        pass

    pypi_org.app.setup_db()

    yield client
