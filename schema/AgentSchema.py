from mongoengine import *

class AgentSchema(Document):
    name = StringField()
    project_id = StringField()
    agent_id = StringField()
