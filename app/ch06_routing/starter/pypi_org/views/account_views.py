import flask

from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

# ######## Index ########

@blueprint.route('/account')
@response(template_file='home/index.html')
def index():
    return {}


# ######## Register ########

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}

@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_get():
    return {}

# ######## Login ########

@blueprint.route('/account/login', method=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


# ######## Logout ########

@blueprint.route('/account/logout')
def logout():
    return {}
