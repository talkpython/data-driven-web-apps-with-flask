import uuid

import flask
from flask import session

import pypi_org.infrastructure.cookie_auth as cookie_auth
from pypi_org.configs import app_config
from pypi_org.infrastructure import session_cache, msal_builder
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import user_service
from pypi_org.viewmodels.account.index_viewmodel import IndexViewModel
from pypi_org.viewmodels.account.login_viewmodel import LoginViewModel
from pypi_org.viewmodels.account.register_viewmodel import RegisterViewModel
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ################### AZURE AUTH ############################


@blueprint.route('/account/auth')
def auth():
    args = flask.request.args

    if flask.request.args.get('state') != session.get("state"):
        return flask.redirect('/')  # No-OP. Goes back to Index page
    if "error" in flask.request.args:  # Authentication/Authorization failure

        return f"There was an error logging in: Error: {args.get('error')}, details: {args.get('error_description')}."
    if flask.request.args.get('code'):
        cache = session_cache.load_cache()
        result = msal_builder.build_msal_app(cache=cache).acquire_token_by_authorization_code(
            flask.request.args['code'],
            scopes=app_config.SCOPE,  # Misspelled scope would cause an HTTP 400 error here
            redirect_uri='http://localhost:5006/account/auth')
        if "error" in result:
            return f"There was an error logging in: Error: {args.get('error')}, details: {args.get('error_description')}."

        session_cache.save_cache(cache)
        # 'oid': '257af28c-d791-4287-bf95-b67578dae57e',
        claims = result['id_token_claims']

        email = claims.get('emails', ['NONE'])[0].strip().lower()
        first_name = claims.get('given_name')
        last_name = claims.get('family_name')

        user = user_service.find_user_by_email(email)
        if not user:
            user = user_service.create_user(f'{first_name} {last_name}', email, str(uuid.uuid4()))

        resp = flask.redirect('/account')
        cookie_auth.set_auth(resp, user.id)
        return resp

    return flask.redirect('/')


@blueprint.route('/account/begin_auth')
def begin_auth():
    state = str(uuid.uuid4())
    session["state"] = state

    return flask.redirect(msal_builder.build_auth_url(state=state))


# ################### INDEX #################################


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('/account/login')

    return vm.to_dict()


# ################### REGISTER #################################

@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        vm.error = 'The account could not be created'
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGIN #################################

@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    vm = LoginViewModel()
    return vm.to_dict()


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    vm = LoginViewModel()
    vm.validate()

    if vm.error:
        return vm.to_dict()

    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ################### LOGOUT #################################

@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect(  # Also logout from your tenant's web session
        app_config.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=http://localhost:5006/")
    cookie_auth.logout(resp)
    session.clear()  # Wipe out user and its token cache from session
    return resp
