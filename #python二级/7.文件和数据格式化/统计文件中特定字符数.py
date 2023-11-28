def calSofFile(s):
    f = open('cwy_copy.txt', 'r').read()
    count = 0
    for i in f:
        if s == i:
            count += 1
        else:
            continue
    return count


print(calSofFile(input()))