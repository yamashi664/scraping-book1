import os,time,urllib,requests
from bs4 import BeautifulSoup

target_url = 'https://uta.pw/shodou/index.php?master'
save_dir = './image-meisaku'

#メイン処理
def download_images():
    html = requests.get(target_url).text
    urls = get_url(html)
    DL_img(urls)
    
#画像のURLを取得
def get_url(html):
    li = []
    soup = BeautifulSoup(html, 'html5lib')
    imgs = soup.find_all('img')
    for img in imgs:
        s = img['src']
        url = urllib.parse.urljoin(target_url, s)
        print('img.src=', url)
        li.append(url)
    return li

#画像データをダウンロード
def DL_img(urls):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    
    for url in urls:
        fname = os.path.basename(url)
        save_file = os.path.join(save_dir,fname)
        r = requests.get(url).content
        with open(save_file, 'wb',) as fp:
            fp.write(r)
            print("save:", save_file)
        time.sleep(1)

if __name__ == '__main__':
    download_images()
