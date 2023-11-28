import requests
import json
req = requests.get('https://api.bilibili.com/x/web-interface/ranking/region?rid=1&day=3&original=0')
data = req.json()
l = data['data']
i = 0
while i < 11:
    print(l[i]['title'],l[i]['pic'])
    i += 1
