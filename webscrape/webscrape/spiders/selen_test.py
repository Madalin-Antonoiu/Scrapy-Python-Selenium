
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

PATH = 'C:\\Users\\antonoium\\Desktop\\chromedriver'
USER = 'antonoium'
PASSWORD = 'madutzu93classiC'

driver = webdriver.Chrome('C:\\Users\\antonoium\\Desktop\\chromedriver.exe')
driver.get('https://servicedesk.csiltd.co.uk/WOListView.do?requestViewChanged=true&viewName=38020_MyView&globalViewName=All_Requests') # Group Unassigned

user_field = "//input[@id='username']"
password_field = "//input[@id='password']"
login_button = "//button[@id='loginSDPage']"

UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(user_field))
UserElement.send_keys(USER)

PasswordElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(password_field))
PasswordElement.send_keys(PASSWORD)

LoginElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button))
LoginElement.click()

driver.get('https://servicedesk.csiltd.co.uk/WOListView.do?requestViewChanged=true&viewName=38020_MyView&globalViewName=All_Requests')
# driver.execute_script("Document.prototype.queryXPath = function (path) { var list = new Array(); var xpath = document.evaluate( path, document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null ); for (var i=0; i<xpath.snapshotLength; i++) { list.push(xpath.snapshotItem(i)); }; return list }; var tableRows = document.queryXPath(`//*[@id='RequestsView_TABLE']/tbody/tr`); console.log(tableRows);")

myfile = open("C:\\Users\\antonoium\\Desktop\\venv\\highlight_script.js", "rt")
contents = myfile.read()
myfile.close()
print(contents)
driver.execute_script(contents)

# Get Js Code from other file as string for selenium browser execute
# myfile = open("lorem.txt", "rt") # open lorem.txt for reading text
# contents = myfile.read()         # read the entire file into a string
# myfile.close()                   # close the file
# print(contents)                  # print contents