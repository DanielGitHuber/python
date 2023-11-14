f = open('html_label', 'r').read().split(',')
f2 = open('html1.html', 'r').readlines()
f3 = open('html提取内容', 'w')
d = {}
for i in f:
    for j in f2:
        if i in j:
            d[i] = d.get(i, 0) + 1
            f3.write(i + j)
        else:
            pass;
f3.close()
items = list(d.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))
