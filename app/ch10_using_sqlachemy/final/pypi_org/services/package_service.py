from typing import List
import sqlalchemy.orm

import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def get_latest_releases(limit=10) -> List[Release]:
    session = db_session.create_session()

    releases = session.query(Release). \
        options(sqlalchemy.orm.joinedload(Release.package)).\
        order_by(Release.created_date.desc()). \
        limit(limit). \
        all()

    session.close()

    return releases


def get_package_count() -> int:
    session = db_session.create_session()
    return session.query(Package).count()


def get_release_count() -> int:
    session = db_session.create_session()
    return session.query(Release).count()
