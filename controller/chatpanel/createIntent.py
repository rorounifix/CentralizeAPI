import requests as req
from configparser import ConfigParser
from controller.log import log
import json

config = ConfigParser()
config.read('config/config.ini')
token_access = config["MAIN"]['token_access']
url_bot = config["MAIN"]["url_bot"]

def createIntent(botname, intents):
    try:
        headers = {
            "Content-Type":"application/json",
            "Authorization":token_access
        }

        body = json.dumps({
                    	"displayName":intents
                    })
        new_url_bot = "{}{}/agent/intents".format(url_bot, botname)
        res = req.post(new_url_bot, headers=headers, data=body)
        return res.json() if int(res.status_code) == 200 else False

    except Exception as e:
        print(e)
        log("controller/chatpanel/createbot.py", e)
        return False

if __name__ == "__main__":
    createIntent("newbot-b1c3c", "test")
