from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    url = 'https://uta.pw/sakusibbs/'
    driver.get(url)
    a = driver.find_element(By.LINK_TEXT, '名作アーカイブ')
    a.click()
    time.sleep(10)
    print(a.text)