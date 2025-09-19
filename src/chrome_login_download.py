import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_url = 'https://uta.pw/sakusibbs/users.php?action=login'
user_id, password = ('JS-TESTER', 'ipCU12ySxI')

save_dir = os.path.dirname(os.path.abspath(__file__))
save_file = save_dir + '/list.csv'

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'download.default_directory': save_dir})

#メイン処理
def login_download():
    driver = webdriver.Chrome(options=options)
    login(driver)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'マイページ')))
    
    link_click(driver,'マイページ')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'CSVでダウンロード')))

    link_click(driver,'CSVでダウンロード')
    for i in range(30):
        if os.path.exists(save_file):break
        time.sleep(1)
        
#ログイン処理    
def login(driver):
    driver.get(login_url)
    usr = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'username_mmlbbs6')))
    pwd = driver.find_element(By.NAME, 'password_mmlbbs6')
    usr.send_keys(user_id)
    pwd.send_keys(password)
    pwd.submit()
    print('login_OK')
        
#リンクのクリック処理
def link_click(driver, label):
    a = driver.find_element(By.PARTIAL_LINK_TEXT, label)
    a.click()
    print('click_OK')

if __name__ == '__main__':
    driver = None
    try:
        login_download()
    finally:
        if driver:
            driver.quit()