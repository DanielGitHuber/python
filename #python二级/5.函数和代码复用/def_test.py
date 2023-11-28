def multiply(x, y=10):
    print(x * y)


multiply(99)
multiply(99, 2)
multiply(y=2, x=99)


def multiply1(x, y=10):
    return x * y, x + y


s = multiply1(99)
a, b = multiply1(99)
print(s, a, b)


def manyret(x):
    try:
        if x > 0:
            return x + 1
        else:
            return x - 1
    except:
        return 0


print(manyret(1))
print(manyret(-1))
print(manyret(0))
print(manyret('x'))
# global全局声明


# lambda表达式-匿名函数


'''def f(n):
    n += 1


m = f(2)
print(m)'''


def f(n):
    def f2(m):
        m += 1
        return m
    n += f2(n)
    return n


print(f(2))