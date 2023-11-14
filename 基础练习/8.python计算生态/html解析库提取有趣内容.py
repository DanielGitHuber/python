# 未完成，转爬虫
from bs4 import BeautifulSoup
f = open('html1.html', 'r').read()
soup = BeautifulSoup(f, 'lxml')
print(soup.contents[2].name)