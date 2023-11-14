from time import *
# 时间处理
print(time())

print(gmtime())

print(ctime())

# 时间格式化
print('--------------')
t = localtime()
print(mktime(t))
print(ctime(mktime(t)))

t_s = strftime('%Y-%m-%d %H:%M:%S', t)
print(t_s)

print(strptime(t_s, '%Y-%m-%d %H:%M:%S'))  # localtime格式

# 计时


def coreLoop():
    limit = 10 ** 8
    while limit > 0:
        limit -= 1


def otherLoop_1():
    sleep(0.2)


def otherLoop_2():
    sleep(0.4)


def main():
    print('begin time:', strftime('%Y-%m-%d %H:%M:%S', localtime()))
    t1 = perf_counter()
    otherLoop_1()
    t2 = perf_counter()
    der_1 = t2 - t1
    t3 = perf_counter()
    coreLoop()
    t4 = perf_counter()
    der_2 = t4 - t3
    t5 = perf_counter()
    otherLoop_2()
    t6 = perf_counter()
    der_3 = t6 - t5

    der_total = t6 - t1
    print('end time:', strftime('%Y-%m-%d %H:%M:%S', localtime()))
    print('model_1 running time:{}'.format(der_1))
    print('model_core running time:{}'.format(der_2))
    print('model_2 running time:{}'.format(der_3))
    print('models totally running time:{}'.format(der_total))


main()