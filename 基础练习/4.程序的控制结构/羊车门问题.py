from random import *
m = n = 0  # 更换选择的次数为m，不更换选择的次数n
k = randint(800000, 1000000)
for i in range(k+1):
    a, b = randrange(1, 4), randrange(1, 4)  #a,b分别为随机产生的自己选中的门序号和车所在序号
    if a == b:
        n += 1
    else:
        m += 1
print('不更换选择选中车的概率为：{}\n更换选择选中车的概率为：{}'.format(n/k, m/k))
