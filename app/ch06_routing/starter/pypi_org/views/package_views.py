import flask

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
def package_details(package_name: str):
    test_packages = package_service.get_latest_packages()
    return "Package details for {}".format(package_name)

@blueprint.route('/<int:rank>')
def popular(rank: int):
    print(type(rank), rank)
    return "The details for the {}th most popular package".format(rank)