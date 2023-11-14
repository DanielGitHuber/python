# 转储
f = open('data.csv', 'w')
# l = eval(input('请输入一个需要转储为csv格式的列表：'))
l = ['1', '2,1']
l_new = []
for i in l:
    if ',' in i:
        l_new.append(i.replace(',', '@'))
    else:
        l_new.append(i)
f.write(','.join(l_new))
f.close()
# 解析
f = open('data.csv', 'r').read().split(',')
l_print = []
for i in f:
    if '@' in i:
        l_print.append(i.replace('@', ','))
    else:
        l_print.append(i)
print(l_print)