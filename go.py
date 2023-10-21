#first
print('hello')



#变量val
val='hello'
print(val)



#数据data
##字符串及方法
n='weiyang chen'
first_n='chen'
last_n='weiyang'
full_n=first_n+' '+last_n+' '
print(full_n)
full_n=full_n.strip()
print(full_n)
print('\n\t')
print(n.title())
print(n.upper())
print(n.lower())
##数字及运算
a=2+3
b=2*3
c=2-3
d=3/2
e=2**3
f=0.2+0.3
message='happy '+str(a)+'th birthday'#避免类型错误
print(a,b,c,d,e,f,'\t',message)



#列表list
foundation=['daniel','gadia','asimov','贝莱',2023]##创建
print(foundation)
print(foundation[0],foundation[-1])##索引
print('My favorite writer is '+foundation[2].title()+'.')
foundation[0]='R.Daniel'##修改
foundation.append(1016)##添加
foundation.insert(-1,162056)##插入
foundation.insert(-1,1016)
print(foundation)
del foundation[-3]##不使用删除
time=foundation.pop()##使用删除
print(time)
time=foundation.pop(-1)
print(time)
print(foundation)
foundation.remove(2023)##按值删除
print(foundation)
foundation.sort(reverse=True)##永久性排序
print(foundation)
print(sorted(foundation))##暂时性排序
print(foundation)
foundation.reverse()##倒转列表
print(foundation)
print(len(foundation[0]))##获取长度
##！注意避免索引错误，可以打印列表或其长度进行检查



#操作列表
##遍历
for name in foundation:
    print(name)
##创建数值列表，左取右不取
nums=list(range(0,5,2))
print(nums)
squares=[]##一串数的平方加入到列表
for num in nums:
    squares.append(num**2)
print(squares,min(squares),max(squares),sum(squares))##最小值，最大值，求和
##列表解析 nums=[num_2 for num_2 in range(1,10,2)]
print([num_2 for num_2 in range(1,10,2)])
test=list(range(1,1000001))
print(sum(test))
##切片，左取右不取
print(squares[0:3],squares[:2],squares[2:],squares[-1:],squares[:])

#元组(不可变的列表）
length=(200,50,60,80)
print(length[0:3])



#if语句（条件测试）
##检查与比较
print(length[0]==200,length[0]==100,length[0]!=200,length[0]!=100)
print(length[0]<length[1],length[0]<=length[2],length[0]>length[3],length[0]>=length[3])
##多个条件
print(length[0]>=300 and length[1]>=30)
print(length[0]>=300 or length[1]>=30)
##检查是否存在特定值和布尔表达式while True:print(length)
print(200 in length,50 not in length)
if length[0]==20:
    print('yes')
elif length[1]==40: ##若ture则跳过余下测试 必要时仅使用if
    print('no')
else:
    print('emmmm')
##检查特殊元素
count = 0
for l in length:
    if l >= 200:
        count = count + 1
    else:
        print('no')
print(count)
##检查列表非空
if length:
    for l in length:
        print(l)
    print('length have ' + str(len(length)) + ' elements')
else:
    print('length is empty')
##使用多个列表—>遍历再判断条件



#字典dictionary(键值对)
tools = {'I':'实体','II':'软件','III':'数据'}
spirits = {
    '本能':'常识',
    '智力':'知识',
    '理性':'观念',
    }
print(tools,tools['I'])##获取
tools['s1'] = 'to'##添加
tools['s2'] = 'ing'
print(tools)
splits = {}##空字典
splits[1] = 'group'
splits[2] = 'individual'
splits[3] = 'object'
print(splits)
##可赋值修改（增值修改）
##del语句删除值
##遍历字典
print(spirits.items())##items返回键值对列表
print(spirits.keys())##keys返回键列表
print(spirits.values())##values返回值列表
for key,value in spirits.items():
    print('\nKey:' + key)
    print('Value:' + value)
##嵌套
##字典列表
worlds = [splits, spirits, tools]##用range和append复制创建
print(worlds)
##列表(元组）字典
lists = {
    1:foundation,
    2:nums,
    3:squares,
    4:length,
    }
print('\n\n',lists)
##字典字典
dicts = {
    1:tools,
    2:spirits,
    3:splits,
    }
print('\n\n',dicts)


'''
#输入与while循环
##input函数
go = input('Type and enter to continue...')##默认字符串输入
print('You just typed : ' + go + ' And the type of your input is', type(go))
##获取数值输入
intgo = int(go)
print(intgo, type(intgo))
print(4%3,6%9)##求模运算

while True:   ##条件成立时持续循环，除非有退出语句
##while value != 300
##while active
    if int(input('guess the value')) == 300:
        ##exit()退出程序
        break##退出循环
        ##continue返回头并继续循环
    else:
        print('nope, keep guessing!')
'''
##处理列表与字典
##在列表之间移动元素&删除包含特定值的列表元素
##使用用户输入填充字典



#函数def
def greet():
    print('hello')
greet()
def greet_name(name):       ##形参：函数入口，存储并传递实参
    print('hello, ' + name)
greet_name('cwy')       ##实参：传给函数的信息
##位置实参
def m_p(master, pet):
    print(master + '\'s pet\'s name is ' + pet)
m_p('mkx','al')
m_p('cwy','jj')
##关键字实参
m_p(pet='fl', master='cwy')
##默认值
def m_p(master, pet='gogogo'):      ##注意先后顺序
    print(master + '\'s pet\'s name is ' + pet)
m_p('mkx')
##注意等效的函数调用以及避免实参不匹配
##返回值return 将形参等于某值（空）以将实参变为可选的
##返回字典
##传递列表
def greet(names):
    for name in names:
        print('hello, ' + name.title())
greet_names = ['mkx', 'cwy', 'al']
greet(greet_names)
##在函数中使用pop&append修改列表
##使用[:]创建副本以禁止函数修改列表
##传递任意数量实参（存储到一个元组中）
print('\n')
def hello(*names):
    for name in names:
        print('hello, ' + name)
hello('cwy','mkx','al','gogogo')
##模块：包含函数的python文件 以下为导入模块方式
##1
import go_moudle as gm
gm.hello('cwygogogo')
##2
from go_moudle import hello as h
h('mkxgogogo')
##3 导入模块中所有函数，可直接调用函数
from go_moudle import *
hello('algogogo')
##可导入类class（单个或多个或整个，以及模块中导入模块）



#类class
##实例化：基于类来创建对象
##类中的函数称为方法
class Person():
    def __init__(self,height,age):    ##类获取数据以创建实例（对象cwy），self用于在类的方法之间传递数据
        self.height = height    ##属性：存储实例变量
        self.age = age
        self.weight = 62    ##默认值
    def p_h(self):
        print(self.height)
    def p_a(self):
        print(self.age)
    def change(self,new_weight):
        self.weight = new_weight
    def increment(self,weight):
        self.weight += weight
cwy = Person(160,23)        ##实例化，对应self
print(cwy.age)     ##访问属性
cwy.p_h()       ##调用方法
##修改属性值方式
##1
print(cwy.weight)
cwy.weight = 63
print(cwy.weight)
##2
cwy.change(64)
print(cwy.weight)
##3
cwy.increment(1)
print(cwy.weight)
##继承
class Superme(Person):
    def __init__(self,height,age):
        super().__init__(height,age)
        self.me = Person(166,60)        ##可将实例用作属性
    def p_h(self):      ##同名方法 优先关注子类方法(用于重写）
        print(self.age)
Cwy = Superme(170,25)       ##子类实例
Cwy.p_h()
print(Cwy.weight)       ##默认值也继承
print('Person的实例：',Cwy.me)

import calendar
c = calendar.TextCalendar(calendar.MONDAY)
c.prmonth(2023,10)
print(c.formatyear(2023,1,0,1,4))

print('q')
print('w')
print('z')
































