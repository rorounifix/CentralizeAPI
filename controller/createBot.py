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



def create_new_bot(botname):

    response = {}

    url_log_in = "https://accounts.google.com/signin/oauth/identifier?client_id=1016740739912-2dfjqgvhb5aqn920vvarkfniio1cahlh.apps.googleusercontent.com&as=VW_DLOzKP2B3bbgZKkFG7A&destination=https%3A%2F%2Fconsole.dialogflow.com&approval_state=!ChRUWXpKUEhtZTV2M2Q0TGItVEMwRxIfQTZpeWNVVXpMWDhhOEhuU1JuY2dubW9lZTlTcmhCWQ%E2%88%99APNbktkAAAAAXD1pYU7g8TABnnRs2MfIdIyZnahDCx4F&oauthgdpr=1&oauthriskyscope=1&xsrfsig=ChkAeAh8T8JQ0qmdw0VQZLEPzE10dskpzCtDEg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_driver = os.getcwd() + "\\chromedriver.exe"

    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    driver.get(url_log_in)

    wait = WebDriverWait(driver, 20)

    identifier = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
    identifier.send_keys('pythondeveloper1991@gmail.com')
    identifier.send_keys(Keys.ENTER)
    time.sleep(5)
    passwd = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    passwd.send_keys('0919628939')
    passwd.send_keys(Keys.ENTER)

    time.sleep(10)
    create_agent_url = "https://console.dialogflow.com/api-client/#/newAgent"
    driver.get(create_agent_url)
    time.sleep(5)
    bot_name = wait.until(EC.presence_of_element_located((By.ID, "entity-name")))
    bot_name.send_keys(botname)
    create_btn = wait.until(EC.presence_of_element_located((By.ID, "multi-button")))
    create_btn.click()
    while create_agent_url == driver.current_url:
        time.sleep(1)
        # print(driver.current_url)

    agent_id = driver.current_url.split('/')[-2]
    # print(agent_id)
    driver.get("https://console.dialogflow.com/api-client/agents/{}".format(agent_id))
    get_json = driver.find_element_by_tag_name('pre').text
    bot_details = json.loads(get_json)

    name = bot_details["agent"]["name"]
    project_id = bot_details["agent"]["cloudProjectId"]

    # print(name)
    # print(project_id)

    response["agent_id"] = agent_id
    response["name"] = name
    response["project_id"] = project_id

    return response


if __name__ == "__main__":
    create_new_bot("thisIs")
