import json
import unittest


# 文件
with open('test.txt', 'w') as test:  # r读 w写 a附加 r+读写
    test.write('i love python!\n')
    test.write('i love programming.\n')
    test.write('i also love creating apps that can run in a browser.')
with open('D:/学习/python/#python二级/7.文件和数据格式化/cwy_copy.txt', encoding='UTF-8') as cc:
    print(cc.readlines())




# 异常处理
try:
    print(5 / 0)
except:
    print('ZeroDivisionError!')

def count_words(filename):
    try:
        with open(filename) as f_n:
            contents = f_n.read()
    except:
        print('FileNotFoundError!')  # 什么都不做pass
    else:
        words = contents.split()
        print('The file has about ' + str(len(words)) + ' words.')


count_words('test.txt')


# json库
numbers = [1, 2, 3, 4, 5, 6]
filename = 'numbers.json'
with open(filename, 'w') as n:
    json.dump(numbers, n)
with open(filename) as numbers:
    nums = json.load(numbers)


print(nums)




'''# 代码测试
def get_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

class NameTest(unittest.TestCase):
    def test_name(self):
        formatted_name = get_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # 断言方法的一种


unittest.main()'''