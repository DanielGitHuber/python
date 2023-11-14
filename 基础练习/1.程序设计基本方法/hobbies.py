hobbies = ''
for i in range(3):
    s = input('请输入三个小爱好，按Q或q结束：')
    if s.upper() == 'Q' or s.upper() == 'q':
        break
    hobbies += s + ' '
print('你的小爱好是：', hobbies)