a = eval(input())
if a % 4 == 0 and a % 100 != 0:
    print('你输入的年份是普通闰年')
elif a % 400 == 0:
    print('你输入的年份是世纪闰年')
else:
    print('你输入的年份是平年')

# 2000年-3000年 的闰年
print('2000年-3000年 的普通闰年:')
for i in range(2000, 3001):
    if i % 4 == 0 and i % 100 != 0 and i % 400 != 0:
        print(i, end=' ')
print('\n2000年-3000年 的世纪闰年:')
for i in range(2000, 3001):
    if i % 400 == 0:
        print(i, end=' ')