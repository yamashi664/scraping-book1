from selenium import webdriver
import time

with webdriver.Chrome() as driver:
    driver.get('https://python.org')
    driver.save_screenshot('screenshot.png')
    time.sleep(10)
