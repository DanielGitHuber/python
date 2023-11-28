# 字符串string及方法
n = 'weiyang chen'
first_n = 'chen'
last_n = 'weiyang'


full_n = first_n + ' ' + last_n + ' '
print(full_n)
full_n = full_n.strip()
print(full_n)
print(n.title())
print(n.upper())
print(n.lower())


# 数字number及运算
a = 2 + 3
b = 2 * 3
c = 2 - 3
d = 3 / 2
e = 2 ** 3
f = 0.2 + 0.3
message = 'happy ' + str(a) + 'th birthday'  # 避免类型错误
print(a, b, c, d, e, f, '\t', message)


# 列表list及操作列表
foundation = ['daniel', 'gadia', 'asimov', '贝莱', 2023]  # 创建


print(foundation)
print(foundation[0], foundation[-1])  # 索引
foundation[0] = 'R.Daniel'  # 修改
foundation.append(1016)  # 添加
foundation.insert(-1, 'gaiya')  # 插入
print(foundation)
del foundation[-3]  # 不使用删除
pop = foundation.pop(-1)  # 使用删除
print(pop, foundation)
foundation.remove('gaiya')  # 按值删除
print(foundation)
print('\n')
foundation.sort(reverse=True)  # 永久性排序
print(foundation)
print(sorted(foundation))  # 暂时性排序
print(foundation)
foundation.reverse()  # 倒转列表
print(foundation)
print(len(foundation[0]))  # 获取长度
# 遍历
for name in foundation:
    print(name)
# 创建数值列表，左取右不取
nums = list(range(0, 5, 2))
print(nums)
# 一串数的平方加入到列表
squares = []
for num in nums:
    squares.append(num ** 2)
print(squares, min(squares), max(squares), sum(squares))  # 最小值，最大值，求和
# 列表解析
print([num_2 for num_2 in range(1, 10, 2)])
# 切片，左取右不取
print(squares[0:3], squares[:2], squares[2:], squares[-1:], squares[:])
# 元组(不可变的列表）
length = (200, 50, 60, 80)
print(length[0:3])


# 字典dictionary(键值对)
tools = {'I': '实体', 'II': '软件', 'III': '数据'}
spirits = {
    '本能': '常识',
    '智力': '知识',
    '理性': '观念',
}
splits = {}  # 空字典创建


print(tools, tools['I'])  # 读取
tools['s1'] = 'to'  # 添加
tools['s2'] = 'ing'
print(tools)
splits[1] = 'group'
splits[2] = 'individual'
splits[3] = 'object'
print(splits)
print(spirits.items())  # items返回键值对列表
for key, value in spirits.items():
    print('\nKey:' + key)
    print('Value:' + value)
print(spirits.keys())  # keys返回键列表
print(spirits.values())  # values返回值列表
# 字典列表
worlds = [splits, spirits, tools]
print(worlds)
# 列表(元组）字典
lists = {
    1: foundation,
    2: nums,
    3: squares,
    4: length,
}
print('\n', lists)
# 字典字典
dicts = {
    1: tools,
    2: spirits,
    3: splits,
}
print('\n', dicts)