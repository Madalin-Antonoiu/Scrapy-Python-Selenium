# After each one is assigned, it does a page refresh so bye bye code, it needs to be injected over and over again
# It will throw an error if Refresh 3,5.. min is active. Needs to be on 0

# if cookies not empty ( cookies.txt will be deleted automatically from drive every 12 hours)
# run the short, load way . Delete cookies.txt for fresh cookies if it fails to work

# RUN THE GUI and press the buttons!

# for LOGS.txt, replace pickle with plain read and write ;)

import pickle
import pprint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pathlib import Path
import traceback
import logging
from selenium.webdriver.chrome.options import Options # headless
import datetime



class AutoSD:

    def __init__(self):
        print('initiating the bot...')
        global USER, PASSWORD, COOKIES_PATH, COOKIES, chrome, session_ID, URL, LOGS, LOGS_PATH
        USER = 'antonoium'
        PASSWORD = 'madutzu93classiC'
        COOKIES = "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\cookies.txt"
        CHROMEDRIVER_PATH = "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\chromedriver.exe"
        COOKIES_PATH = Path(COOKIES)
        LOGS = "C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\logs.txt"
        LOGS_PATH = Path(LOGS)

        # Headless ( no GUI)
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        #driver = webdriver.Chrome(options=options)
        chrome = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)  # This will open the Chrome window
        chrome.minimize_window()  # for the browser to start minimized


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

    def obtain_sd_cookies(self):

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



    # Only for logs.txt
    @staticmethod
    def get_logs(ticket_id, agent, current_technician, subject, priority):
        x = datetime.datetime.now()
        formatted = "%a, %d %b %Y, at %H:%M"
        date_time = x.strftime(formatted)
        print(date_time)

        text = date_time + " - " + " [" + priority + "] " + ticket_id + " : " + agent + " , " + current_technician + " , " + "[" + subject + "]"

        if LOGS_PATH.is_file():

            # Fix for : EOFError: Ran out of input
            try:
                logs = pickle.load(open(LOGS, "rb"))  # read from logs already
                saved_text = logs + "\n" + text
                return saved_text
            except EOFError:
                saved_text = text
                return saved_text

        else:
            # In case logs.txt doesn't exist in the location
            saved_text = text
            return saved_text

    @staticmethod
    def save_logs(text, location):
        pickle.dump(text, open(location, "wb"))


    # Main functions
    @staticmethod
    def open_assigned_to(nr): # This is recreation of my highlight_script.js as Selenium
        row = nr # starts with 0 being first, 4 means 5th row
        popup_path = "//table[@class='DialogBox']"
        ticket_id_path = "//td[@id='RequestsView_r_"+row+"_5']//div"
        subject_path = "//td[@id='RequestsView_r_"+row+"_6']//div/a"
        assig_cell = "//td[@id='RequestsView_r_"+row+"_7']//div/div"
        priority_path = "// td[ @ id = 'RequestsView_r_"+row+"_8']//div/table/tbody/tr/td[last()]"
        all_rows = "//*[@id='RequestsView_TABLE']/tbody/tr[position() > 2]"


        print(assig_cell)

        # Cookies might have expired if you get an error here
        assigned_cell = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(assig_cell))
        agent = assigned_cell.text.strip()


        # Counting total tickets number
        all_rows_len = WebDriverWait(chrome, 10).until(lambda chrome:chrome.find_elements_by_xpath(all_rows))
        count = len(all_rows_len)
        print('---- Group Unassigned : ' + str(count) + ' tickets -----')

        #repeating_tickets and their count


        ticket_id = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(ticket_id_path)).text.strip()
        subject = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(subject_path)).text.strip()
        priority = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(priority_path)).text.strip()

        if agent == 'Unassigned':
            assigned_cell.click()
            popup = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(popup_path))
            return popup, agent, ticket_id, subject, priority, row, 'Step1: Popup clicked:'

        raise Exception("Fail - Not Unassigned")

    @staticmethod
    def get_technician(msg2):
        technician = "//div[@id='s2id_selectTechnician']"
        tech_name_xpath = "//div[@id='s2id_selectTechnician']//a[@class='select2-choice']//span"

        if msg2 is not None:
            current_tech = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(tech_name_xpath)).text.strip() # these 2 lines represent the first span text of technician
            # technician_elem.click()

            return current_tech, 'Step2: Current technician: '

        raise Exception("Technician is NULL 394934834")

    @staticmethod
    def open_group(current_technician):
        if current_technician == "NONE":
            group_xpath = "//div[@id='s2id_assignGroup']//a[@class='select2-choice']"
            open_group = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_element_by_xpath(group_xpath)).click()
            return open_group, 'Step3: Group list opened'

        raise Exception("Fail - Current technician is not NONE")

    @staticmethod
    def select_service_desk(msg):
        if msg == "Step3: Group list opened":
            groups_ul_xpath = "//div[@id='select2-drop']//ul//li"
            groups = WebDriverWait(chrome, 10).until(lambda chrome: chrome.find_elements_by_xpath(groups_ul_xpath))
            #return groups[5].text 'Csi Facilities'

            for group in groups:
                if group.text == "Service Desk":
                    group.click()
                    return 'Step4: Chosen Service Desk'

        raise Exception("Fail - groups list was not opened")


    #def GROUP_UNASSIGNED(self):

    def main(self, nr):
        try:
            if not COOKIES_PATH.is_file():
                print('Cookies.txt not found, obtaining cookies.')
                self.obtain_sd_cookies()  # If cookies.txt not to be found, log in and create em

                # Otherwise skip logging and use cookies
            self.load_cookies(chrome, COOKIES)
            chrome.get(
                'https://servicedesk.csiltd.co.uk/WOListView.do?requestViewChanged=true&viewName=38020_MyView&globalViewName=All_Requests')

            # Main execution chain
            popup, agent, ticket_id, subject, priority, row, msg1 = self.open_assigned_to(nr)
            print(msg1 + " " + priority + " " + ticket_id + " - " + agent + " , " + "[" + subject + "]")  # "Opened AssignedTo popup for:"

            current_technician, msg2 = self.get_technician(msg1)
            print(msg2 + " " + current_technician)  # 'Current technician: '

            group, msg3 = self.open_group(current_technician)
            print(msg3)

            msg4 = self.select_service_desk(msg3)
            print(msg4)

            txt = self.get_logs(ticket_id, agent, current_technician, subject, priority)
            self.save_logs(txt, LOGS)

            #self.inject_javascript()

            return "[" + row + "]" + priority + " " + ticket_id + " - " + agent + " , " + "[" + subject + "]"

        except Exception as e:
            logging.error(traceback.format_exc())
            # Logs the error appropriately.


















        # Get Js Code from other file as string for selenium browser execute
        # myfile = open("lorem.txt", "rt") # open lorem.txt for reading text
        # contents = myfile.read()         # read the entire file into a string
        # myfile.close()                   # close the file
        # print(contents)                  # print contents

    #def repeated(self):
