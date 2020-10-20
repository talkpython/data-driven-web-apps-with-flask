import uuid

import msal

from pypi_org.configs import app_config


def build_auth_url(authority=None, scopes=None, state=None):
    return build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri="http://localhost:5006/account/auth")


def build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
        client_credential=app_config.CLIENT_SECRET, token_cache=cache)
