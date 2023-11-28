a = eval(input('请输入一个数字'))
b = eval(input('请输入另一个数字'))
c = 1
d = a * b
if a > b :
    while True:
        c = a % b
        if c == 0:
            print('最大公约数是：', b)
            print('最小公倍数是：', int(d/b))
            break
        a = b
        b = c
elif a < b:
    while True:
        c = b % a
        if c == 0:
            print('最大公约数是：', a)
            print('最小公倍数是：', int(d/a))
            break
        b = a
        a = c
else:
    print('最大公约数是：', a)
    print('最小公倍数是：', int(d/a))
