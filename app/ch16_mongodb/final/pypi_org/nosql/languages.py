import datetime
import mongoengine


class ProgrammingLanguage(mongoengine.Document):

    id = mongoengine.StringField(primary_key=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    description = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'languages',
        'indexes': [
            'created_date',
        ]
    }
