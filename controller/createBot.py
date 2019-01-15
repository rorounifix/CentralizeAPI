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
import requests
##from controller.log import log



##def create_new_bot(botname):

response = {}

url_log_in = "https://console.dialogflow.com/api-client/#/login"
chrome_options = Options()
##    chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() + "..\\..\\chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
driver.get(url_log_in)

wait = WebDriverWait(driver, 20)

identifier = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "md-btn-login-text-wrapper")))
identifier.click()

identifier = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
identifier.send_keys('pythondeveloper1993@gmail.com')
identifier.send_keys(Keys.ENTER)
time.sleep(5)
passwd = wait.until(EC.presence_of_element_located((By.NAME, "password")))
passwd.send_keys('0919628939')
passwd.send_keys(Keys.ENTER)

headers = {
"User-Agent":
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
req = requests.session()
req.headers.update(headers)

token_url = "https://console.dialogflow.com/api-client/agents/dcc46338-0699-4d22-8d48-674d79c6f2e6/opAccessToken"
agents_url = "https://console.dialogflow.com/api-client/agents"

for c in driver.get_cookies():
    cookie = {c["name"]:c["value"]}
    req.cookies.update(cookie)

token = req.get(token_url)
agents = req.get(agents_url)

print(token.status_code)
print(token.json())


##    time.sleep(10)
##    create_agent_url = "https://console.dialogflow.com/api-client/#/newAgent"
##    driver.get(create_agent_url)
##    time.sleep(5)
##    bot_name = wait.until(EC.presence_of_element_located((By.ID, "entity-name")))
##    bot_name.send_keys(botname)
##    create_btn = wait.until(EC.presence_of_element_located((By.ID, "multi-button")))
##    create_btn.click()
##    while create_agent_url == driver.current_url:
##        time.sleep(1)
##        # print(driver.current_url)
##
##    agent_id = driver.current_url.split('/')[-2]
##    # print(agent_id)
##    driver.get("https://console.dialogflow.com/api-client/agents/{}".format(agent_id))
##    get_json = driver.find_element_by_tag_name('pre').text
##    bot_details = json.loads(get_json)
##
##    name = bot_details["agent"]["name"]
##    project_id = bot_details["agent"]["cloudProjectId"]
##
##    # print(name)
##    # print(project_id)
##
##    response["agent_id"] = agent_id
##    response["name"] = name
##    response["project_id"] = project_id
##
##    return response


##if __name__ == "__main__":
##    create_new_bot("thisIs")
