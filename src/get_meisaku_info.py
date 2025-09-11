import os, csv, requests
from bs4 import BeautifulSoup

target_url = 'https://uta.pw/shodou/index.php?master'
save_file = 'meisaku.txt'

html = requests.get(target_url).text
soup = BeautifulSoup(html, 'html5lib')

arts = soup.select('.article')
data = []
for art in arts:
    titles = art.select('.art_title')
    if len(titles) < 2:
        continue
    t = titles[1].text
    img_url = art.select('img')[0]['src']
    data.append([t,img_url])

with open(save_file, 'wt', encoding='utf-8') as fp:
    csv.writer(fp, delimiter='\t').writerows(data)    
