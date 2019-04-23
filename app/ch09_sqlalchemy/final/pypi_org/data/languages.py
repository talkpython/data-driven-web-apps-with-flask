import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase


class ProgrammingLanguage(SqlAlchemyBase):
    __tablename__ = 'languages'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
