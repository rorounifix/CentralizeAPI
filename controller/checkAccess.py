from configparser import ConfigParser
import requests as req
import json
from controller.log import log

def checkAccess():

    try:

        config = ConfigParser()
        config.read('config/config.ini')
        url = config['MAIN']['url']
        token_access = config['MAIN']['token_access']

        headers = {
            "Content-Type":"application/json",
            "Authorization":token_access
        }

        body = json.dumps({
                "queryInput":{
                    "text":{
                        "text":"hi",
                        "languageCode":"en"
                        }
                    },
                "queryParams":{
                    "timeZone":"Asia/Shanghai"
                    }
            })

        response = req.post(url, headers=headers, data=body)
        return True if int(response.status_code) == 200 else False

    except Exception as e:
        log("checkAccess", e)
        return False


if __name__ == "__main__":
    checkAccess()
