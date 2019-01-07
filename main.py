
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


flow = flow_from_clientsecrets('client.json',
                               scope='https://www.googleapis.com/auth/dialogflow',
                               redirect_uri='http://localhost'  )


auth_uri = flow.step1_get_authorize_url()
print(auth_uri)
# code = "4/ywAE4bZnF9-c9ssdwTq0FEpf9rJ0NkVT0pzJCqA2crP2_gD1QgmOnjc4C976a4XymtCs6qb0Rh0z-seaDwtol60&scope=https://www.googleapis.com/auth/dialogflow"
#
# credentials = flow.step2_exchange(code)
##print(credentials.to_json())

# curl -H "Content-Type: application/json; charset=utf-8"  -H "Authorization: Bearer ya29.c.ElqKBmr7mEITpjlwxrMyjsTDHnfu0CT4CZtwTdlvsd8ijHJyr3C55sDgXlYQBxG_PlkbOK0gPOtuBzctgPNSPdF3e47dJ-eqCmaB3fI2-ikj1zHvRr6SImS1z2Y"  -d "{\"queryInput\":{\"text\":{\"text\":\"hi\",\"languageCode\":\"en\"}},\"queryParams\":{\"timeZone\":\"Asia/Shanghai\"}}" "https://dialogflow.googleapis.com/v2/projects/newagent-3b884/agent/sessions/aea471be-80e7-e74b-de26-a931419989e5:detectIntent"


chrome_options = Options()
##chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
driver.get(auth_uri)

wait = WebDriverWait(driver, 20)
code = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
code.send_keys('rorounifix')
code.send_keys(Keys.ENTER)
##code = wait.until(EC.presence_of_element_located((By.xpath("//*[@data-email='rorounifix@gmail.com']"))))





