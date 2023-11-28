# 输入
"""
input('\n请输入并按enter键')
"""

# 导入相应模块
import sys

'''
import sys;x='iloveu';sys.stdout.write(x+'\n')
from sys import argv,path
print('----------python from import----------')
print('path:',path)
'''
# 循环和条件语句
'''
a,b=0,1
while b<10:
     print(b)
     a,b=b,a+b;#先算右边，再赋给左边
     
age=int(input('请输入你家狗狗年龄:'))
print('')
if age < 0:
         print("请输入正确的年龄")
elif age ==1:
         print("相当于14岁的人")
elif age ==2:
         print("相当于22岁的人")
elif age > 2:
         human=22+(age-2)*5
         print("对应人类年龄：",human)
         '''
# 数字：int/float/bool/complex(复数)
# 运算：+/-/*/ / / // /%/**
'''a, b, c = 20, 5.5, True
print(type(a),type(b),type(c),'\n')
print(isinstance(a,int))'''

# 字符串：''或""，\转义 不能被改变
'''print('C:\some\name')
print(r'C:\some\nmae','\n')

str = 'iloveu'
print(str[0], end=" ")
print(str[1:5:2], end=" ")
print(str[-1], end=" ")


print("\nfuck u\nworld!\n"*2)'''

# 列表：类型可以不同，元素可修改
'''a = ['him', 25]
print(a)

a = a+[100,'her']
print(a)

a[0]='I'
a[1:]=['love''u']
print(a)'''

# 元组：与列表类似，但是写在小括号里，元素不可修改
'''tup=(1999,2021,'physics','math')
print('\n',tup,type(tup),len(tup))

tup=('i','love','u','very','much')
print(tup[0],tup[1:])

tup=()#空元组
tup=(1,)#一个元素

tup1,tup2=(1,2,3),(4,5,6)
print(tup1+tup2)'''

# 集合：无序不重复元素的集，基本功能是进行成员测试，消除重复元素,也可进行集合运算
'''s={1,2,3,4,5,6,1,2,3}
print('\n',s)
print(6 in s)

a=set('adjljdllfg')
b=set('ahjfakjskl')
print(a,'\n',b,'\n',a-b,'\n',a|b,'\n',a&b,'\n',a^b)'''

# 字典：无序的键-值对集合，关键字必须是不可变类型（包含可变类型的tuple又不能），同一字典关键字不能相同
'''dic={}#空字典
tel={'jack':1,'tom':2,'rose':3}
print(tel,'\n',tel['jack'],'\n')

del tel['rose']#删除一个键值对
tel['mary']=3#添加
print(tel)

print(list(tel.keys()))#返回key组成的list
print(tel.keys())
print(tel.values())

dic = {x: x**2 for x in (2,4,6)}
print(dic)'''

# 连接数据库
'''import pymysql
db=pymysql.connect("localhost","vae","123","employees")
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print('database version',data)
db.close()'''

# 循环
'''n = 10
sum1 = 0
sum2 = 0
mul1 = 1
mul2 = 1
counter = 1
while counter <= n:
    sum1 = sum1 + counter
    mul1 = mul1 * counter
    counter += 1
for i in range(1, 11):
    sum2 = sum2 + i
    mul2 = mul2 * i
print('sum of 1 until %d:%d' % (n, sum1))
print('sum of 1 until %d:%d' % (n, sum2))
print('mul of 1 until %d:%d' % (n, mul1))
print('mul of 1 until %d:%d' % (n, mul2))

for i in range(len(a)):
    print(i, a[i])
'''
# 找质数
'''for i in range(2, 100):
    for x in range(2, i):
        if i % x == 0:
            print(i, '=', x, '*', i//x)
            break
    else:
        print(i, 'is prime number')'''

# 迭代器
l = list(range(5))
it = iter(l)
'''print(next(it))
print(next(it))

for i in it:
    print(i, end=" ")'''

'''while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        sys.exit()'''

# 生成器
'''def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)
# f 是一个迭代器，由生成器返回值生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()'''

# test
'''def a(n):
    i = 1
    while i <= n:
        yield i
        i += 1


f = a(10)
print(next(f))
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()'''



