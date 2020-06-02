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
from time import sleep, strftime

class AutoSD:

    def __init__(self):
        print('initiating the bot...')
        self.USER = 'antonoium'
        self.PASSWORD = 'madutzu93classiC'
        chromedriver_path = "C:\\Users\\antonoium\\Desktop\\chromedriver"
        global driver, cookies_location
        cookies_location = Path("C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\cookies.txt")
        driver = webdriver.Chrome(executable_path=chromedriver_path)  # This will open the Chrome window
        #sleep(2)

    # This should run once per day


    def save_cookies(self, location):
        self.pickle.dump(driver.get_cookies(), open(location, "wb"))

    @staticmethod
    def load_cookies(driver, location, url='https://servicedesk.csiltd.co.uk/'):
        cookies = pickle.load(open(cookies_location, "rb"))
        driver.delete_all_cookies()
        url = "https://google.com" if url is None else url
        driver.get(url)
        for cookie in cookies:
            driver.add_cookie(cookie)

    #This is my main function to be called
    def get_sd_cookies(self):

        driver.get('https://servicedesk.csiltd.co.uk/')  # Group Unassigned

        user_field = "//input[@id='username']"
        password_field = "//input[@id='password']"
        login_button = "//button[@id='loginSDPage']"

        user_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(user_field))
        user_element.send_keys(self.USER)

        password_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password_field))
        password_element.send_keys(self.PASSWORD)

        login_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button))
        login_element.click()

        pprint.pprint(driver.get_cookies())  # to visualise them in console
        self.save_cookies(driver, "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\cookies.txt")
        driver.quit();


    def main(self):

        if not cookies_location.is_file():
            self.get_sd_cookies()

        # Login to SD using cookies and getting into groups Unassigned
        self.load_cookies(driver, cookies_location)
        driver.get(
            'https://servicedesk.csiltd.co.uk/WOListView.do?requestViewChanged=true&viewName=38020_MyView&globalViewName=All_Requests')

        # get script content from separate file
        myfile = open("C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\highlight_script.js", "rt")
        contents = myfile.read()
        myfile.close()

        # Browser inject with the script defined at highlight_script.js
        driver.execute_script(contents) # replace with selenium doing things


        # Get Js Code from other file as string for selenium browser execute
        # myfile = open("lorem.txt", "rt") # open lorem.txt for reading text
        # contents = myfile.read()         # read the entire file into a string
        # myfile.close()                   # close the file
        # print(contents)                  # print contents

