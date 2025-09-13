import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.google.com/'

with webdriver.Chrome() as driver:
    driver.get(url)
    name = driver.find_element(By.NAME, 'q')
    name.send_keys('Pythonの教科書')
    name.submit()
    time.sleep(10)

