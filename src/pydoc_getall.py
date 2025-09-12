import requests, urllib, os, time
from bs4 import BeautifulSoup

save_dir = './pydoc_tutorial'
top_page = 'https://docs.python.org/ja/3/tutorial/index.html'
check_url = 'https://docs.python.org/ja/3/tutorial/'

visited = set()

def get_page(url):
    if check_url not in url: return
    if url in visited: return
    visited.add(url)
    
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    html = res.text

    fname = save_dir + '/' + os.path.basename(url)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    with open(fname, 'w', encoding='utf-8') as fp:
        fp.write(html)
        print('save:', fname)
    
    time.sleep(1)
    
    soup = BeautifulSoup(html, 'html5lib')
    for a in soup.select('a'):
        a_url = urllib.parse.urljoin(url, a['href'])
        a_url = urllib.parse.urldefrag(a_url)[0]
        get_page(a_url)

if __name__ == '__main__':
    get_page(top_page)