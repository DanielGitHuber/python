def getText1():
    txt = open("The Way of All Flesh.txt", "r", encoding='GBK').read()
    txt = txt.lower()
    for ch in '!"#%&()*+,.-/:;<=>?@[\\]^_\'{|}~':
        txt = txt.replace(ch, ' ')
    return txt


Txt1 = getText1()
words = Txt1.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))


def getText2():
    txt = open("cwy.txt", "r", encoding='utf-8').read()
    txt = ' '.join(txt)
    txt = txt.lower()
    for ch in '！@#￥%……&*（）——-+=《，》。、？‘’“”：；{}【】|~':
        txt = txt.replace(ch, ' ')
    return txt


Txt2 = getText2()
words = Txt2.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))