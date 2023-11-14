from random import *


def s_txt(low, high, txtname):
    f = open('{}.txt'.format(txtname), 'w')
    for line in range(10):
        word = ''
        for row in range(10):
            word += str(randrange(low, high)) + ' '
        f.write(word + '\n')
    f.close()


def s_csv(txtname, csvname):
    f1 = open('{}.txt'.format(txtname), 'r')
    f2 = open('{}.csv'.format(csvname), 'w')
    for line in f1:
        after = line.replace(' ', ',')
        f2.write(after)
    f1.close()
    f2.close()


def main():
    low, high = eval(input('请输入随机数上限low，和下限high：'))
    txtname = input('请输入txt文件名：')
    s_txt(low, high, txtname)
    csvname = input('请输入csv文件名：')
    s_csv(txtname, csvname)


main()