import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class Download(SqlAlchemyBase):
    __tablename__ = 'downloads'

    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    package_id = sqlalchemy.Column(sqlalchemy.String, index=True)
    release_id = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    ip_address = sqlalchemy.Column(sqlalchemy.String)
    user_agent = sqlalchemy.Column(sqlalchemy.String)
