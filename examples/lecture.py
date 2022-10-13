import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Selenium is a "property based" tool, a.k.a "second generation". 
# Might wanna look up what that means, since you slept through that
# part of the lecture. 

driver = webdriver.Chrome()

# launch the app
driver.get("http://www.wikipedia.org")
time.sleep(2)

# find elements
driver.find_element_by_id("js-link-box-en").click()
time.sleep(2)

# interact
driver.find_element_by_id("searchInput").send_keys("tiger")
time.sleep(2)
driver.find_element_by_id("searchInput").send_keys(Keys.ENTER)
time.sleep(2)

# check
assert "Tiger - Wikipedia" == driver.title

assert "Tiger" == driver.find_element_by_id("firstHeading").text

print("all good")

driver.close()

# Pretty cool tool. Might be able to use this for a bunch of
# fun online automation things. HLTV stats perhaps? Quickly
# calculating 