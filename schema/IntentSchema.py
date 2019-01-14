from mongoengine import *

class IntentSchema(Document):
    project_id = StringField()
    intent_name = StringField()
