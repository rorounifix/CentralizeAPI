from flask import Flask
from flask_restful import Api
from routes.chatpanel import *
from controller.changeConfig import changeConfig
from controller.checkAccess import checkAccess
from mongoengine import *


app = Flask(__name__)
api = Api(app)

config = ConfigParser()
config.read('config/config.ini')
address = config["Mongo"]['address']
port = config["Mongo"]['port']
database = config["Mongo"]['database']

register_connection(host=address, port=int(port), db=database, alias='default')

if not checkAccess():
    changeConfig()

api.add_resource(Create, '/create')
api.add_resource(Talk, '/')
api.add_resource(CreateIntent, '/intents')
api.add_resource(Train, '/train')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
