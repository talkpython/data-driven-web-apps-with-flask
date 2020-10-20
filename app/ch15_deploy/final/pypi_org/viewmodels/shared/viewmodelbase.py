import uuid
from typing import Optional

import flask
import msal
from flask import Request

from pypi_org.configs import app_config
from pypi_org.infrastructure import request_dict, cookie_auth


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie_auth.get_user_id_via_auth_cookie(self.request)

    def to_dict(self):
        d = self.__dict__
        d['build_auth_url'] = self.build_auth_url

        return d

    # noinspection PyMethodMayBeStatic
    def build_auth_url(self, authority=None, scopes=None, state=None):
        return self.build_msal_app(authority=authority).get_authorization_request_url(
            scopes or [],
            state=state or str(uuid.uuid4()),
            redirect_uri="http://localhost:5006/account/auth")

    # noinspection PyMethodMayBeStatic
    def build_msal_app(self, cache=None, authority=None):
        return msal.ConfidentialClientApplication(
            app_config.CLIENT_ID, authority=authority or app_config.AUTHORITY,
            client_credential=app_config.CLIENT_SECRET, token_cache=cache)

