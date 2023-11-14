# 一维数据
ls = ['beijing', 'shanghai', 'tianjin', 'chongqing']
f = open('city.csv', 'w')
f.write(','.join(ls)+'\n')
f.close()
f = open('city.csv', 'r')
ls = f.read().strip('\n').split(',')
f.close()
print(ls)
# 二维数据
ls = '''地区 新增 累计 治愈 死亡
美国 17357 34490134 28912906	619343
印度 49851 30233183 29251029	395780
巴西 79277 18386894 16582053	512819
法国 1986 5768443 5601802 110951'''
f = open('yiqing.csv', 'w')
for row in ls:
    f.write(row)
f.close()
f = open('yiqing.csv', 'r')
ls = []
for line in f:
    ls.append(line.strip('\n').split(' '))
f.close()
for row in ls:
    line = ''
    for item in row:
        line += '{:10}\t'.format(item)
    print(line)



