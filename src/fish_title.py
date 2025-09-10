from bs4 import BeautifulSoup

with open('fish.html', encoding = 'utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

title = soup.find('title')
print(title)