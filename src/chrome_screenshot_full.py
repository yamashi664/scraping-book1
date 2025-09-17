from selenium import webdriver

url = 'https://python.org'
save_file = 'screenshot_full.png'

def screenshot_full(url,save_file):
    #ページサイズ取得
    w,h = get_page_size(url)
    #指定サイズでchromeを起動しキャプチャ
    screenshot_size(url,save_file,w,h)

def  get_page_size(url):
    driver = webdriver.Chrome()
    driver.get(url)
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    driver.close()
    print("page_size = ", w, h)
    return (w,h)

def screenshot_size(url,save_file,w,h):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #画面サイズ指定
    win_size = 'window-size='+str(w)+','+str(h)
    options.add_argument(win_size)
    
    cap_driver = webdriver.Chrome(options=options)
    cap_driver.get(url)
    cap_driver.save_screenshot(save_file)
    cap_driver.close()

if __name__ == '__main__':
    screenshot_full(url, save_file)