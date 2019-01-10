from flask_restful import Resource
from configparser import ConfigParser


config = ConfigParser()
config.read('config/config.ini')

class ChatPanel(Resource):

    def __init__(self, token_access):
        self.url = config['MAIN']['url']
        self.token_access = config['MAIN']['token_access']

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {"test":'test'}


if __name__ == "__main__":
    ChatPanel()
