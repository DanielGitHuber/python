while True:
 txt = input('请输入明文文本：')
 for t in txt:
    if 'a' <= t <= 'z':
        print(chr(ord(t)+3), end='')
    elif 'A' <= t <= 'Z':
        print(chr(ord(t)+3), end='')
    elif 0x4E00 <= ord(t) <= 0x9FA5:
        print(chr(ord(t)+3), end='')
    else:
        print(t, end='')
