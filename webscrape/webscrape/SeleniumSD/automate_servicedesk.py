# After each one is assigned, it does a page refresh so bye bye code, it needs to be injected over and over again
# It will throw an error if Refresh 3,5.. min is active. Needs to be on 0

# if cookies not empty ( cookies.txt will be deleted automatically from drive every 12 hours)
# run the short, load way . Delete cookies.txt for fresh cookies if it fails to work

# RUN THE GUI and press the buttons!


import pickle
import pprint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
import traceback
import logging


class AutoSD:

    def __init__(self):
        print('initiating the bot...')
        global USER, PASSWORD, COOKIES_PATH, COOKIES, chrome, session_ID, URL
        USER = 'antonoium'
        PASSWORD = 'madutzu93classiC'
        COOKIES = "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\cookies.txt"
        CHROMEDRIVER_PATH = "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\chromedriver.exe"
        COOKIES_PATH = Path(COOKIES)
        chrome = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)  # This will open the Chrome window

        session_ID = chrome.session_id
        URL = chrome.command_executor._url
        #print(session_ID, URL)

    @staticmethod
    def save_cookies(driver, location):
        pickle.dump(driver.get_cookies(), open(location, "wb"))

    @staticmethod
    def load_cookies(driver, location, url='https://servicedesk.csiltd.co.uk/'):
        cookies = pickle.load(open(location, "rb"))
        driver.delete_all_cookies()
        url = "https://google.com" if url is None else url
        driver.get(url)
        for cookie in cookies:
            driver.add_cookie(cookie)

    def get_sd_cookies(self):

        chrome.get('https://servicedesk.csiltd.co.uk/')  # Group Unassigned

        user_field = "//input[@id='username']"
        password_field = "//input[@id='password']"
        login_button = "//button[@id='loginSDPage']"

        user_element = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(user_field))
        user_element.send_keys(USER)

        password_element = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(password_field))
        password_element.send_keys(PASSWORD)

        login_element = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(login_button))
        login_element.click()

        pprint.pprint(chrome.get_cookies())  # to visualise them in console
        self.save_cookies(chrome, COOKIES)
        chrome.quit()

    @staticmethod
    def inject_javascript():
        # get script content from separate file
        my_file = open("C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\highlight_script.js", "rt")
        contents = my_file.read()
        my_file.close()
        chrome.execute_script(contents) # replace with selenium doing things

    @staticmethod
    def open_assigned_to(): # This is recreation of my highlight_script.js as Selenium

        # Strings
        assig_to = "//*[@id='RequestsView_TABLE']/tbody/tr[3]/td[8]"
        assig_popup = "//table[@class='DialogBox']"

        assigned_to = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(assig_to))
        assig_to_str = assigned_to.get_attribute("textContent").strip()

        if assig_to_str == 'Unassigned':
            assigned_to.click()
            assigned_popup = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(assig_popup))
            return {'Step 1': 'Got row element', 'element': assigned_popup}


    def main(self):
        try:
            if not COOKIES_PATH.is_file():
                self.get_sd_cookies() # If cookies.txt not to be found, log in and create em

            # Otherwise skip logging and use cookies
            self.load_cookies(chrome, COOKIES)
            chrome.get('https://servicedesk.csiltd.co.uk/WOListView.do?requestViewChanged=true&viewName=38020_MyView&globalViewName=All_Requests')

            safe0 = self.open_assigned_to()
            print(safe0)

            #self.inject_javascript()

        except Exception as e:
            logging.error(traceback.format_exc())
            # Logs the error appropriately.


















        # Get Js Code from other file as string for selenium browser execute
        # myfile = open("lorem.txt", "rt") # open lorem.txt for reading text
        # contents = myfile.read()         # read the entire file into a string
        # myfile.close()                   # close the file
        # print(contents)                  # print contents

