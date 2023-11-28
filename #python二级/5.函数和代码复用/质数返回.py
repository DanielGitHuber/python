import sys
import time


def Prime(n):
    s = []
    for i in range(2, n+1):
        k = True
        for j in range(2, i):
            if i % j == 0:
                k = False
                break
        if k:
            s.append(i)
    return s


def isPrime(b):
    if b in Prime(b):
        return True
    else:
        return False


def Prime_2(n):
    s = []
    for i in range(2, n+1):
        k = True
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                k = False
                break
        if k:
            s.append(i)
    return s


def isPrime_2(b):
    if b in Prime_2(b):
        return True
    else:
        return False


while True:
    try:
        a = input('请输入一个整数（按q&Q退出程序）：')
        t1 = time.perf_counter()
        print(isPrime(int(a)))
        t2 = time.perf_counter()
        print('所用时间为：{}'.format(1000*(t2-t1)))
        t1 = time.perf_counter()
        print(isPrime_2(int(a)))
        t2 = time.perf_counter()
        print('所用时间为：{}'.format(1000*(t2-t1)))
    except:
        if a == 'q' or a == 'Q':
            sys.exit()
        else:
            print('输入错误，请重新输入！')
