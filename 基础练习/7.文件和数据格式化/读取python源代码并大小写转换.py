import jieba
import keyword
fo = open('test.py', 'r').read()
table = keyword.kwlist
words = jieba.lcut(fo)

fo2 = open('test.py', 'w')
pas = ''
for i in range(0, len(words)):
    if words[i] in table:
        pass
    else:
        words[i] = words[i].upper()
        pas = ''.join(words)
fo2.write(pas)
fo2.close()
