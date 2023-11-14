def parseCSV():
    dataNames, data = [], []
    f = open('人口基本情况数据', 'r', encoding='GBK').readlines()
    for line in f:
        sl = line.strip('\n').split('\t')
        if '指标' in sl[0]:
            years = [int(x[:-1]) for x in sl[1:]]
        else:
            dataNames.append('{:10}'.format(sl[0]))
            data.append([float(x) for x in sl[1:]])
    return years, dataNames, data


def means(data):
    return sum(data)/len(data)


def calNewData(newyears, a, b):
    return [(a+b*x) for x in newyears]


def Regression(xlist, ylist):
    xmeans, ymeans = means(xlist), means(ylist)
    b1 = -len(xlist)*xmeans*ymeans
    b2 = -len(xlist)*xmeans**2
    for x, y in zip(xlist, ylist):
        b1 += x*y
        b2 += x**2
    b = b1/b2
    a = ymeans - b * xmeans
    return a, b


def showResults(years, dataNames, newDatas):
    print('{:^150}'.format('国家人口情况线性估计'))
    header = '指标        '
    for y in years:
        header += '{:20}'.format(y)
    print(header)
    for name, lineData in zip(dataNames, newDatas):
        line = '{:<10}'.format(name)
        for data in lineData:
            line += '{:>20.1f}'.format(data)
        print(line)


def main():
    newyears = [x+2021 for x in range(1, 100, 20)]
    newDatas = []
    years, dataNames, datas = parseCSV()
    for data in datas:
        a, b = Regression(years, data)
        newDatas.append(calNewData(newyears, a, b))
    showResults(newyears, dataNames, newDatas)


main()

