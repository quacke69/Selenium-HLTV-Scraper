import time
from selenium import webdriver

print("Enter HLTV matches-url:")
url = input()

DRIVER_PATH = '/Users/ludvig/Documents/GitHub/Selenium-HLTV-Scraper/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
time.sleep(2)
driver.find_element_by_id("CybotCookiebotDialogBodyButtonDecline").click()
time.sleep(2)
elements = driver.find_elements_by_class_name('time')
# for i in range(0, len(elements)):
elements[0].find_element_by_tag_name('a').click()
time.sleep(2)

# driver.close()