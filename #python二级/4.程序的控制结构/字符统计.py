t = input()
c, c1, c2, c3, c4 = 0, 0, 0, 0, 0
for i in t:
    if 65 <= ord(i) <= 122:
        c += 1
    elif 48 <= ord(i) <= 57:
        c1 += 1
    elif i == ' ':
        c2 += 1
    elif 19968 <= ord(i) <= 40869:
        c3 += 1
    else:
        c4 += 1
print('英文字符个数：', c)
print('数字字符个数：', c1)
print('空格个数：', c2)
print('中文字符个数：', c3)
print('其他字符个数：', c4)