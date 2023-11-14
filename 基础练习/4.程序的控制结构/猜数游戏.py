import random
target = random.randint(1, 1000)
count = 0
while True:
    try:
        guess = eval(input('输入一个1-1000的数字:'))
    except:
        # exit()
        print('输入有误，请输入一个数字，不计入猜测次数哦!')
        continue
    count += 1
    if guess > target:
        print('大了')
    elif guess < target:
        print('小了')
    else:
        print('猜对了')
        break
print('你猜了', count, '次')
