# if语句（条件测试）
length = (200, 50, 60, 80)


print(length[0] == 200, length[0] == 100, length[0] != 200, length[0] != 100)
print(length[0] < length[1], length[0] <= length[2], length[0] > length[3], length[0] >= length[3])
print(length[0] >= 300 and length[1] >= 30)
print(length[0] >= 300 or length[1] >= 30)
print(200 in length, 50 not in length)


if length[0] == 20:
    print('yes')
elif length[1] == 40:  # 若ture则跳过余下测试 必要时仅使用if,elif
    print('no')
else:
    print('emmmm')


count = 0
for l in length:  # 判断列表大于200数的个数
    if l >= 200:
        count = count + 1
    else:
        print('no')
print(count)


if length:  # 判断列表非空
    for l in length:
        print(l)
    print('length have ' + str(len(length)) + ' elements')
else:
    print('length is empty')