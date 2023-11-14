list1 = ['1', '2', '167', '89', '17', '4', '90', '2']


def Judge(l):
    if len(set(l)) != len(l):
        return True
    else:
        return False


def Judge2(l):
    s = str(l)
    for i in l:
        if s.count(i) >= 2:
            return True
        else:
            return False


print(Judge(list1))
print(Judge2(list1))