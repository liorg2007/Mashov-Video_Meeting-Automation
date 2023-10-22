from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


"""
Provide your details
"""
user_name = 
password = 
NUM_OF_ENTRIES = 

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://web.mashov.info/students/login")
driver.maximize_window()
time.sleep(2)

#enter login
driver.find_element('xpath','/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/mat-tab-header/div/div/div/div[2]/span[2]/span').click()
time.sleep(1)
driver.find_element('xpath','/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/div/mat-tab-body[2]/div/div/button/span[2]').click()
time.sleep(1)

#login details:
driver.find_element('xpath','/html/body/section/div[1]/div[3]/div[1]').click()
#user name
driver.find_element('xpath', '/html/body/section/div[1]/div[3]/form/fieldset/input[2]').send_keys(user_name)
#password
driver.find_element('xpath', '/html/body/section/div[1]/div[3]/form/fieldset/span/input[4]').send_keys(password)
#send details
driver.find_element('xpath','/html/body/section/div[1]/div[3]/form/fieldset/button').click()
time.sleep(2)
driver.find_element('xpath', '/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/div/mat-tab-body[2]/div/div/button').click()
time.sleep(2)

#enter the lessons menu
driver.find_element('xpath', '/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav/div/mshv-main-menu/ul/li[26]/button/span[2]/div').click()
p = driver.current_window_handle

for i in range(NUM_OF_ENTRIES):
    time.sleep(0.5)
    #swith to main tab
    driver.switch_to.window(p)
    #enter a lesson
    """
    To get the path do the following:
    Get into the menu of the lessons, select with right click(prefered on the end of the button) the lesson wanted and press 'inspect'
    The text highlghted in the side should start with '<a', if not try the following:
    1.Do the same trying to clinch the slight end of the button
    2.Search the element in the inspect window

    After that right click on the element in the inspect tab and put your mouse on the copy option
    Select copy full XPath, and this is the path you put in the argument
    """
    driver.find_element('xpath' ,'/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card[2]/mat-nav-list/a[1]').click()