# 顶层设计思想
from random import random


def printIntro():
    print('{:*^25}'.format('这个程序模拟两个选手A和B的某种竞技比赛'))
    print('{:*^25}'.format('程序需要两位选手的能力值（小数表示）'))


def getInputs():
    a = eval(input('A的能力值（0-1）：'))
    b = eval(input('B的能力值（0-1）：'))
    n = eval(input('模拟比赛的场次：'))
    return a, b, n


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
            print('-------第{}场比赛-------A胜利'.format(i))
        else:
            winsB += 1
            print('-------第{}场比赛-------B胜利'.format(i))
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA/(probB + probA):
                scoreA += 1
            else:  # 当A输球时，发球权交给B
                serving = 'B'
        else:
            if random() < probB/(probA + probB):
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b ==15  # 双方任意先赢得15分结束比赛


def printSummary(winsA, winsB):
    n = winsA + winsB
    print('竞技分析结束，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场，占比{:0.1%}'.format(winsA, winsA/n))
    print('选手B获胜{}场，占比{:0.1%}'.format(winsB, winsB/n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


main()
