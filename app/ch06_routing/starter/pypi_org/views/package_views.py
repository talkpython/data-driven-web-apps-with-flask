import flask

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    test_packages = package_service.get_latest_packages()
    return "Package details for {}".format(package_name)
    # return flask.render_template('home/index.html', packages=test_packages)