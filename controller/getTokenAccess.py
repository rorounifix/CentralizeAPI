from oauth2client.client import flow_from_clientsecrets
import httplib2
from apiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import json
from urllib.parse import unquote
from controller.log import log


def getTokenAccess():

    try:

        flow = flow_from_clientsecrets('config/client.json', scope='https://www.googleapis.com/auth/dialogflow', redirect_uri='http://localhost'  )
        auth_uri = flow.step1_get_authorize_url()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.getcwd() + "\\chromedriver.exe"

        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        driver.get(auth_uri)

        wait = WebDriverWait(driver, 20)

        identifier = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
        identifier.send_keys('pythondeveloper1991@gmail.com')
        identifier.send_keys(Keys.ENTER)
        time.sleep(5)
        passwd = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        passwd.send_keys('0919628939')
        passwd.send_keys(Keys.ENTER)

        time.sleep(10)
        current_url = driver.current_url
        driver.delete_all_cookies()
        code = unquote(current_url.split('=')[1])


        credentials = flow.step2_exchange(code)
        access_token = "Bearer {}".format(json.loads(credentials.to_json())["access_token"])
        return access_token


    except Exception as e:
        log("getTokenAccess.py", e)
        return False



if __name__ == "__main__":
    print(getTokenAccess())
