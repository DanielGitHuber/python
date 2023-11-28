go = input('Type and enter to continue...')  # 默认字符串输入
intgo = int(go)  #获取数字输入


print('You just typed : ' + go + ' And the type of your input is', type(go))
print(intgo, type(intgo))




while True:   # 条件成立时持续循环，除非有退出语句
# while value != 300
# while active
    if int(input('guess the value')) == 300:
        print('you are right!')
        break # 退出循环
        # exit()退出程序
        # continue返回头并继续循环
    else:
        print('nope, keep guessing!')