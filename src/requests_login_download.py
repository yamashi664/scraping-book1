import os, time, requests, urllib
from bs4 import BeautifulSoup

login_url = 'https://uta.pw/sakusibbs/users.php?action=login&m=try'
payload = {"username_mmlbbs6":"JS-TESTER", "password_mmlbbs6":"ipCU12ySxI"}
save_file = './src/list2.csv'

#メイン処理
def main():
    session = requests.session()
    res = session.post(login_url, data = payload)
    print(res.status_code)
    time.sleep(1)

    maypage_url = get_url(res.text,'マイページ')
    print("yes")
    maypage_html = session.get(maypage_url)

    csv_url = get_url(maypage_html.text, 'CSVでダウンロード')
    print("yes")
    csv_download(session, csv_url)


#HTMLからリンクURLの取得
def get_url(html, label):
    soup = BeautifulSoup(html, 'html5lib')
    a_list = soup.find_all('a')
    for a in a_list:
        if label in a.text:
            li = a['href']
            link_url = urllib.parse.urljoin(login_url,li)
    time.sleep(1)
    return link_url
    

#CSVをダウンロード
def csv_download(session, url):
    res = session.get(url)
    print(res.encoding)
    with open(save_file, 'wt') as fp:
        fp.write(res.text)
    time.sleep(1)

if __name__ == '__main__':
    main()
