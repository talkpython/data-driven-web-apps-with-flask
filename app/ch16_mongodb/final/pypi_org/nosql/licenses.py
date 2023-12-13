import datetime
import mongoengine


class License(mongoengine.Document):
    id = mongoengine.StringField(primary_key=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    description = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'licenses',
        'indexes': [
            'created_date',
        ],
    }
