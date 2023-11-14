def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return Fibonacci(n-1) + Fibonacci(n-2)  # 递归方法使用


def printFib():
    n = eval(input('请输入一个整数：'))
    print(Fibonacci(n))


printFib()