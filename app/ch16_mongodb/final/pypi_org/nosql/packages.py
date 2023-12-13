import datetime

import mongoengine


class Package(mongoengine.Document):
    id = mongoengine.StringField(primary_key=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    summary = mongoengine.StringField()
    description = mongoengine.StringField()

    home_page = mongoengine.StringField()
    docs_url = mongoengine.StringField()
    package_url = mongoengine.StringField()

    author = mongoengine.StringField()
    author_email = mongoengine.StringField()
    license = mongoengine.StringField()

    maintainers = mongoengine.ListField(mongoengine.ObjectIdField())

    meta = {
        'db_alias': 'core',
        'collection': 'packages',
        'indexes': [
            'created_date',
            'author_email',
            'license',
        ],
    }

    def __repr__(self):
        return '<Package {}>'.format(self.id)
