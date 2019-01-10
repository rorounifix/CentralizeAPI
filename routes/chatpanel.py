from flask_restful import Resource
from flask import request
from configparser import ConfigParser
from controller.chatpanel.chatbot import send
from controller.response import response

class ChatPanel(Resource):

    def __init__(self):
        pass

    def get(self):
        return {"test":'test'}

    def post(self):
        res = response()
        try:
            data = {
                "sender_msg":request.json["message"],
                "bot_msg":"null"
            }

            bot_res = send(data["sender_msg"])
            data["bot_msg"] = bot_res["queryResult"]["fulfillmentText"]
            res['status'] = 1
            res["message"] = "success"
            res['data'] = data
        except Exception as e:
            res['message'] = e

        return res



class Train(Resource):

    def __init__(self):
        pass

    def get(self):
        return {"test":'test'}


    def post(self):
        return {"test":'test'}



if __name__ == "__main__":
    ChatPanel()
