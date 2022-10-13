import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
time.sleep(2)
driver.find_element_by_id("nav-search-bar-form").click()
time.sleep(2)
driver.find_element_by_id("twotabsearchtextbox").type("Galactic Purple Dual Sense")
time.sleep(2)
driver.find_element_by_xpath("//*[text() = 'PlayStation DualSense Wireless Controller – Galactic Purple']").click()
time.sleep(2)
print(driver.find_element_by_id("priceblock_ourprice").text)
price = driver.find_element_by_id("priceblock_ourprice").text
price2 = price.replace('$', '')

assert float(price2) > 70

print("all good")

driver.close()