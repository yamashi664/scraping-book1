import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

with webdriver.Chrome(options=options) as driver:
    driver.get('https://uta.pw/sakusibbs/users.php?user_id=1')
    a_list = driver.find_elements(By.CSS_SELECTOR, "ul#mmlist li a")
    for a in a_list:
        print('■',a.text)
        print(('→',a.get_attribute('href')))
        
