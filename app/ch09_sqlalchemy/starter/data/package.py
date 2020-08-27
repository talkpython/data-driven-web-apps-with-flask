import sqlalchemy as sa

class Package:

    # primary key: globally unique - we changed to string as we use the package ID as name)
    # could be an issue later to make a big migration
    id = sa.Column(sa.String, primary_key=True)
    created_date =     datetime
    desc = string



