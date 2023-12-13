import datetime
import mongoengine


class Download(mongoengine.Document):
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    package_id = mongoengine.StringField()
    release_id = mongoengine.IntField()

    ip_address = mongoengine.StringField()
    user_agent = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'documents',
        'indexes': [
            'created_date',
            'package_id',
            'release_id',
        ],
    }
