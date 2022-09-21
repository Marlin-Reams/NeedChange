from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from myinfo import myemail, mypassword


#START THE CHROMINUM SERVICE
driver = webdriver.Chrome(r"M:\marli\Downloads\chromedriver_win32 (3)\chromedriver.exe")

#GET THE SIS PAGE
driver.get("https://sis.galvanize.com/accounts/login/")

#MAXIMIZE THE BROWERS WINDOW FOR CLARITY
driver.maximize_window()

#FIND THE BUTTON TO ACUIRE LOGIN PAGE & CLICK
button = driver.find_element(By.TAG_NAME, 'button')
button.click()

#ENTER EMAIL AND PASSWORD INTO PROPER FIELDS BY ELEMENT ID
email = driver.find_element(By.ID, "user_email").send_keys(myemail)
password = driver.find_element(By.ID, "user_password").send_keys(mypassword)

#FIND THE BUTTON TO SUBMIT USER NAME AND PASSWORD BY CLASS AND CLICK
button = driver.find_element(By.CLASS_NAME, 'btn-primary')
button.click()

#SEE IF THERE IS A WAY TO OPEN ZOOM/// ATM CAN'T BY PASS ALERT MEASSAGE TRYING TO
#FIND A WAY TO EITHER CLICK LEFT AND ENTER OR JUST CLOSE THE ALERT POPUP
# driver.get("https://zoom.us/j/92181671113")
# time.sleep(15)

#GO TO THE ATTENDACE WEBSITE
driver.get("https://sis.galvanize.com/cohorts/8/attendance/mine/")

#IF THE ATTENDACE TOKEN DOES NOT EXIST LOOP UNTILL IT DOES
while not (driver.find_elements(By.CSS_SELECTOR, ".is-size-6")):
    # time.sleep(0)
    driver.refresh()

#GET THE ATTENDANCE TOKEN OFF THE SCREEN
token = driver.find_element(By.CLASS_NAME, "is-danger")
doc = BeautifulSoup(token.text, "html.parser")

#PRINT ATTENDANCE TOKEN FOR CLARITY
print(token.text)

#ADD THE TOKEN TO THE INPUT FIELD
token = driver.find_element(By.CLASS_NAME, "input").send_keys(token.text)

#CLICK THE BUTTON TO SUBMIT THE ATTENDACE TOKEN
button = driver.find_element(By.CLASS_NAME, 'is-primary')
button.click()
time.sleep(15)
