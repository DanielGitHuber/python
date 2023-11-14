import requests
import re
#print(requests.get('https://makerbean.com/').content.decode('UTF-8'))
#print(requests.post('http://exercise.kingname.info/exercise_requests_post',json={'name':'vae','password':'123456'}).content.decode())

html = requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode()
title = re.search('title>(.*?)<',html,re.S).group(1)
content_list = re.findall('<p>(.*?)<',html,re.S)
content_str = '\n'.join(content_list)
print(f'页面标题为：{title}')
print(f'页面正文内容为：\n{content_str}')