def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(fact(100))  # 调用整数阶乘函数
