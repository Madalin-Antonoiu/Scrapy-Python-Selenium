# After each one is assigned, it does a page refresh so bye bye code, it needs to be injected over and over again
# It will throw an error if Refresh 3,5.. min is active. Needs to be on 0
# Double verify AND log every time you do a row - check if unnassigned, when popup open, check if NONE :) This way we absolutely make sure 0% chance of error

# if cookies not empty ( cookies.txt will be deleted automatically from drive every 12 hours)
# run the short, load way

# Delete cookies.txt for fresh cookies if it fails to work

import pickle
import pprint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path

# This should run once per day
cookies_location = Path("C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\cookies.txt")

def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url='https://servicedesk.csiltd.co.uk/'):
    cookies = pickle.load(open(cookies_location, "rb"))
    driver.delete_all_cookies()
    url = "https://google.com" if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)


def get_sd_cookies():
    PATH = 'C:\\Users\\antonoium\\Desktop\\chromedriver'
    USER = 'antonoium'
    PASSWORD = 'madutzu93classiC'

    driver = webdriver.Chrome('C:\\Users\\antonoium\\Desktop\\chromedriver.exe')
    driver.get('https://servicedesk.csiltd.co.uk/')  # Group Unassigned

    user_field = "//input[@id='username']"
    password_field = "//input[@id='password']"
    login_button = "//button[@id='loginSDPage']"

    UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(user_field))
    UserElement.send_keys(USER)

    PasswordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password_field))
    PasswordElement.send_keys(PASSWORD)

    LoginElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button))
    LoginElement.click()

    pprint.pprint(driver.get_cookies())  # to visualise them in console
    save_cookies(driver, "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\cookies.txt")
    driver.quit();


if not cookies_location.is_file():
    get_sd_cookies()

driver = webdriver.Chrome('C:\\Users\\antonoium\\Desktop\\chromedriver.exe')
load_cookies(driver, cookies_location)
driver.get(
    'https://servicedesk.csiltd.co.uk/WOListView.do?requestViewChanged=true&viewName=38020_MyView&globalViewName=All_Requests')

# get script content from separate file
myfile = open("C:\\Users\\antonoium\\Desktop\\venv\\highlight_script.js", "rt")
contents = myfile.read()
myfile.close()

# Browser inject with the script defined at highlight_script.js
driver.execute_script(contents)

# Get Js Code from other file as string for selenium browser execute
# myfile = open("lorem.txt", "rt") # open lorem.txt for reading text
# contents = myfile.read()         # read the entire file into a string
# myfile.close()                   # close the file
# print(contents)                  # print contents
