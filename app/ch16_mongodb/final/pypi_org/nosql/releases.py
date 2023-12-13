import datetime

import mongoengine


class Release(mongoengine.Document):
    package_id = mongoengine.StringField()

    major_ver = mongoengine.IntField()
    minor_ver = mongoengine.IntField()
    build_ver = mongoengine.IntField()

    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    comment = mongoengine.StringField()
    url = mongoengine.StringField()
    size = mongoengine.IntField()

    meta = {
        'db_alias': 'core',
        'collection': 'releases',
        'indexes': [
            'created_date',
            'package_id',
            'major_ver',
            'minor_ver',
            'build_ver',
            {'fields': ['major_ver', 'minor_ver', 'build_ver']},
            {'fields': ['-major_ver', '-minor_ver', '-build_ver']},
        ],
    }

    @property
    def version_text(self):
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
