import flask

from pypi_org.services import package_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase

# Change this to your domain when you go live
# See this github issue for background;
# https://github.com/talkpython/data-driven-web-apps-with-flask/issues/56#issuecomment-3936953307
HOSTED_DOMAIN: str = 'localhost'


class SiteMapViewModel(ViewModelBase):
    def __init__(self, limit: int):
        super().__init__()
        self.packages = package_service.all_packages(limit)
        self.last_updated_text = '2019-07-15'
        self.site = '{}://{}'.format(flask.request.scheme, HOSTED_DOMAIN)
