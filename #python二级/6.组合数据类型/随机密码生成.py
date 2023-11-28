from random import *


def retS():
    a = []
    for i in range(97, 123):
        a.append(chr(i))
    for i in range(65, 90):
        a.append(chr(i))
    return a


def retN():
    b = []
    for i in range(48, 58):
        b.append(chr(i))
    return b


def cCode(x, y):
    if x == y:
        return x
    else:
        return '不相同的密码'


s = retS()
n = retN()
for i in range(10):
    code1 = sample(s, 5) + sample(n, 3)
    shuffle(code1)
    print(''.join(code1))

code2 = sample(s, 5) + sample(n, 3)
shuffle(code2)
code3 = sample(s, 5) + sample(n, 3)
shuffle(code3)
print(cCode(code2, code3))
