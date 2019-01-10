import requests as req
from configparser import ConfigParser
from controller.log import log
import json

config = ConfigParser()
config.read('config/config.ini')
url = config["MAIN"]['url']
token_access = config["MAIN"]['token_access']

def send(msg):
    try:
        headers = {
            "Content-Type":"application/json",
            "Authorization":token_access
        }

        body = json.dumps({
            "queryInput":{
                "text":{
                    "text":str(msg),
                    "languageCode":"en"
                    }
                },
            "queryParams":{
                "timeZone":"Asia/Shanghai"
                }
        })

        res = req.post(url, headers=headers, data=body)
        return res.json() if int(res.status_code) == 200 else False

    except Exception as e:
        print(e)
        log("controller/chatpanel/chatbot.py", e)
        return False





if __name__ == "__main__":
    send("hi there")
