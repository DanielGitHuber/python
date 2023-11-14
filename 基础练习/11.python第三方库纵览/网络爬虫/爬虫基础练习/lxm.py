import os
from lxml import etree

text = '''
<p>
    <ul>
    <li><a href="/files/chinese/" target="_parent">0</a></li>
    <li><a href="/files/7.html" target="_parent">1</a></li>
    <li><a href="/files/world/" target="_parent">2</a></li>
    <li><a href="/files/youth/" target="_parent">3</a></li>
    <li><a href="/files/dushi/" target="_parent">4</a></li>
    <li><a href="/files/13.html" target="_parent">5</a></li>
    </ul>
</p>
'''
html = etree.HTML(text)
s = etree.tostring(html).decode()
print(s)

html_data = html.xpath('/html/body/ul/li/a/text()')
for i in html_data:
    print(i)

html_data = html.xpath('/html/body/ul/li/a/@href')
for i in html_data:
    print(i)

html_data = html.xpath('//li/a[@href="/files/chinese/"]/text()')
print(html_data)

html_data = html.xpath('//li/a/text()')
print(html_data)