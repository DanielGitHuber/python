# 函数function：某种功能的代码块
# 形参：赋值前的变量，定义函数时
# 实参：赋值后的变量，调用函数时（或默认值）
def greet():
    print('hello')

def greet_name(name):
    print('hello, ' + name)

def m_p_1(master, pet):
    print(master + '\'s pet\'s name is ' + pet)

def m_p_2(master, pet='gogogo'):  # 形参在前，实参在后
    print(master + '\'s pet\'s name is ' + pet)


greet()
greet_name('cwy')
m_p_1('mkx', 'al')
m_p_1(pet='fl', master='cwy')
m_p_2('mkx')


def greet_names(names):
    for name in names:
        print('hello, ' + name)

def hello(*names):
    for name in names:
        print('hello, ' + name)


names = ['mkx', 'cwy']  # 传递列表
greet_names(names)
hello('cwy', 'mkx')




