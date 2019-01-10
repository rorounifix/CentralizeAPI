from flask_restful import Resource

class Login(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {"test":"post"}
