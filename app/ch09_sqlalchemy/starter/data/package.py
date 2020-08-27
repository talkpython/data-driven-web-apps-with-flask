import sqlalchemy as sa


class Package:
    # primary key: globally unique - we changed to string as we use the package ID as name)
    # could be an issue later to make a big migration
    # step 1: define data types
    # step 2: wrap them in sqlalchemy syntax
    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime)
    summary = sa.Column(sa.String)
    desc = sa.Column(sa.String)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String)

    license = sa.Column(sa.String)

    # these we add later as they have relations
    # maintainers
    # releases