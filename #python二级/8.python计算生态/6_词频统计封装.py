def getTxt():
    txt = open("The Way of All Flesh.txt", "r", encoding='GBK').read()
    txt = txt.lower()
    for ch in '!"#%&()*+,.-/:;<=>?@[\\]^_\'{|}~':
        txt = txt.replace(ch, ' ')
    return txt


def splitTxt(txt):
    return txt.split()


def calWord(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items


def printItems(items):
    for i in range(10):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))


def main():
    txt = getTxt()
    words = splitTxt(txt)
    items = calWord(words)
    printItems(items)


main()
