from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://python.org')
    driver.save_screenshot('screenshot.png')
    
