import requests
import os
import re
start_url = 'http://www.kanunu8.com/book3/6879'
def get_toc(html):
    #get each chapter html and return a list
    toc_url_list = []
    toc_block = re.findall('正文(.*?)</tbody>',html,re.S)
    toc_url = re.findall('href="(.*?)"',str(toc_block),re.S)
    for url in toc_url:
        toc_url_list.append(start_url+'/'+url)
    return toc_url_list

def get_article(html):
    #get each chapter content and return chaptername&content
    chaptername = re.findall('size="4">(.*?)<',html,re.S)[0]
    text_block = re.findall('<p>(.*?)</p>',html,re.S)
    text_block = text_block[0].replace('<br />','')
    return chaptername,text_block
def save(chapter,article):
    #save each chapter
    os.makedirs('动物农场', exist_ok=True)
    with open(os.path.join('动物农场', chapter + '.txt'), 'w', encoding='utf-8') as f:
        f.write(article)

for url in get_toc(requests.get('http://www.kanunu8.com/book3/6879').content.decode('GBK')):
    c,a = get_article(requests.get(url).content.decode('GBK'))
    save(c,a)