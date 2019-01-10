from flask import Flask
from flask_restful import Api
from routes.chatpanel import *
from controller.changeConfig import changeConfig
from controller.checkAccess import checkAccess


app = Flask(__name__)
api = Api(app)

if not checkAccess():
    changeConfig()


api.add_resource(ChatPanel, '/', resource_class_kwargs={"token_access":"token_access"})

if __name__ == '__main__':
    app.run(debug=True)