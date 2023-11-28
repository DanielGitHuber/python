import requests
import json
req = requests.get('https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1')
data = req.json()
l = data['data']['list']
i = 0
while i < 11:
    print(l[i]['title'],l[i]['pic'])
    i += 1