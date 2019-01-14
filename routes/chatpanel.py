from flask_restful import Resource
from flask import request
from configparser import ConfigParser
from controller.chatpanel.chatbot import send
from controller.chatpanel.createIntent import createIntent
from controller.response import response
from controller.createBot import create_new_bot
from schema.AgentSchema import *

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


class CreateIntent(Resource):

    def __init__(self):
        pass

    def get(self):
        return {"test":'test'}


    def post(self):
        res = response()

        try:
            data = {
                "bot_name":request.json["bot_name"],
                "intent_name":request.json["intent_name"]
            }

            bot_res = createIntent(data["bot_name"], data["intent_name"])
            print(bot_res)
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

            if len(AgentSchema.objects(name__exact=data['name'])) > 0: raise Exception("Name Already Exists")

            bot_res = create_new_bot(data["name"])
            # print(bot_res)
            # {'agent_id': '6ab72f50-b861-41a2-9aa1-86177a30c72d', 'name': 'testss', 'project_id': 'testss-b8948'}
            save_bot = AgentSchema(
                name = bot_res['name'],
                project_id = bot_res['project_id'],
                agent_id = bot_res['agent_id']

                # name = data['name'],
                # project_id = "bot_res['project_id']",
                # agent_id = "bot_res['agent_id']"
            )

            save_bot.save()
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
