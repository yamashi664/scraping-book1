from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"C:\Users\flwfe\AppData\Local\Programs\Python\Python313\chromedriver.exe")  # ←実際のパス
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org")
time.sleep(10)
driver.quit()