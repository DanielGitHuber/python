# 类class：描述某类对象的变量与函数集合
# 实例instance：基于类创建的具体化对象
# 属性attribute：类中的变量
# 方法function：类中的函数
class Person(object):
    def __init__(self, height, age):  # self负责在类中为实例管理变量和函数，实例在外部可以访问或调用它们
        self.height = height
        self.age = age
        self.weight = 62  # 默认值

    def p_h(self):  # 打印身高
        print(self.height)

    def p_a(self):  # 打印年龄
        print(self.age)

    def p_w(self):  # 打印体重
        print(self.weight)

    def r_h(self):  # 体重+1并返回
        self.weight += 1
        return self.weight

    def p_r_h(self):  # 打印r_h()函数返回值
        print(self.r_h())

    def change(self, new_weight):  # 改变体重初始值
        self.weight = new_weight

    def increment(self, weight):  # 增加体重
        self.weight += weight


cwy = Person(160, 23)  # 生成具体的对象，即实例
print(cwy.height)  # 访问属性
cwy.p_h()  # 调用方法
cwy.p_a()
cwy.p_r_h()
cwy.weight = 65  # 修改属性值
cwy.p_w()
cwy.change(66)
cwy.p_w()
cwy.increment(1)
cwy.p_w()


# 继承inheritance
class SuperPerson(Person):
    def __init__(self, height, age):
        super().__init__(height, age)  # 继承父类属性的方式
        self.mkx = Person(166, 60)  # 可将实例用作属性

    def p_h(self):  # 同名方法，优先关注子类方法(用于重写）
        print(self.age)


print('\n')
CWY = SuperPerson(2000, 300)  # 子类实例
CWY.p_h()
print(CWY.weight)  # 默认值也继承
print('父类Person创建的实例的年龄：', CWY.mkx.age)