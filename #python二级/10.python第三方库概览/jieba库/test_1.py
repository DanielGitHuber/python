from jieba import *
from wordcloud import *
f = open('cwy_copy.txt', 'r').read()
t = lcut(f)
print(type(t))
c = {}
for i in t:
    if i in ['，', '。', '\n'] or len(i) == 1:
        continue
    else:
        c[i] = c.get(i, 0) + 1
items = list(c.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    w, c = items[i]
    print(w, c)

newtxt = ''.join(t)
wc = WordCloud().generate(newtxt)
wc.to_file('cwy词云.png')