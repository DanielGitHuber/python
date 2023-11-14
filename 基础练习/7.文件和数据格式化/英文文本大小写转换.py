# -------version1--------
def reSBinEnglishFile():
    f = open('以父之名英文歌词.txt', 'r+').read()
    for i in f:
        if 97 <= ord(i) <= 122:
            print(i.upper(), end='')
        elif 65 <= ord(i) <= 90:
            print(i.lower(), end='')
        elif ord(i) == 32:
            print(' ', end='')
        elif ord(i) == 10:
            print('\n', end='')
        else:
            print(',', end='')


reSBinEnglishFile()


# -------version2--------
def reSBinEnglishFile_2():
    f = open('以父之名英文歌词.txt', 'r+').read()
    s = []
    for i in f:
        if 97 <= ord(i) <= 122:
            s.append(i.upper())
        elif 65 <= ord(i) <= 90:
            s.append(i.lower())
        else:
            s.append(i)
    for j in s:
        print(j, end='')


reSBinEnglishFile_2()