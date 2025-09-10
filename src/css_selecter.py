from bs4 import BeautifulSoup
import csv

with open('fish.html', encoding = 'utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

rows = []
rows.append(['名前','説明','価格'])

div_list = soup.select('#fishes > div')
for div in div_list:
    fish = div.h2.text
    desc = div.select('.desc')[0].text
    price = div.select('.price')[0].text
    rows.append([fish,desc,price])

with open('fish.csv', 'wt', encoding='sjis', newline='') as fp:
    csv.writer(fp).writerows(rows)
    