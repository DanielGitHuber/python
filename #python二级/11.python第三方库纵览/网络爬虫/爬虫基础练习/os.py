import os

#1
print('eq1:')
path = os.getcwd()
print(path)

#2
print('\n','eq2:')
file_list = os.listdir (path)
print(file_list)

#3
print('\n','eq3:')
for i in file_list:
    separate = os.path.splitext(i)
    print(separate,type(separate))

#4
print('\n','eq4:')
if '//home//vae//桌面//职业//python开发//练习//os.py':
    oldname = '//home//vae//桌面//职业//python开发//requests模块'
    newname = '//home//vae//桌面//职业//python开发//爬虫基础练习'
    os.rename(oldname, newname)
