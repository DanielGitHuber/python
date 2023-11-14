import time
from multiprocessing import Pool
import requests
def calc_sqr(num):
    return num * num
p = Pool(10)
origin_num = range(10000)
result = p.map(calc_sqr,origin_num)
print(f'计算0-9的平方分别为：{result}')

def query(url):
    requests.get(url)
start = time.time()
for i in range(100):
    query('https://baidu.com')
end = time.time()
print(f'单线程循环访问百度首页100次，耗时：{end - start}')

start =time.time()
url_list = []
for i in range(100):
    url_list.append('https://baidu.com')
p2 = Pool(5)
p2.map(query,url_list)
end = time.time()
print(f'5线程循环访问百度首页100次，耗时：{end - start}')


