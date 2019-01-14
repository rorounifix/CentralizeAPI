from flask_restful import Resource
from flask import request
from configparser import ConfigParser
from controller.chatpanel.chatbot import send
from controller.chatpanel.createbot import createbot
from controller.response import response
from controller.createBot import create_new_bot

class Talk(Resource):

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
        res = response()

        try:
            data = {
                "message":request.json["message"],
                "response":request.json["response"]
            }

            bot_res = send(data["sender_msg"])
            data["bot_msg"] = bot_res["queryResult"]["fulfillmentText"]
            res['status'] = 1
            res["message"] = "success"
            res['data'] = data
        except Exception as e:
            res['message'] = e

        return res

class Create(Resource):

    def __init__(self):
        pass

    def post(self):

        res = response()

        try:
            data = {
            	"name":request.json['name']
            }


            bot_res = create_new_bot(data["name"])
            print(bot_res)
            # if bot_res == False: raise Exception('already Exists')
            res['status'] = 1
            res["message"] = "success"
            # res['data'] = bot_res["displayName"]
        except Exception as e:
            print(e)
            res['message'] = str(e)

        return res



if __name__ == "__main__":
    Train()
