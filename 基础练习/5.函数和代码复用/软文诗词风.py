txt = '''
人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。
'''
# txt = input()
linewidth = 30  # 预定输出宽度


def linesplit(line):
    plist = ['，', '！', '？', '。', '，', '！', '？']
    for p in plist:
        line = line.replace(p, '\n')
    return line.split('\n')


def lineprint(line):
    global linewidth
    while len(line) > linewidth:  # 当短句字数超过限制时，分行居中显示
        print(line[0:linewidth])
        line = line[linewidth:]
    print(line.center(linewidth, chr(12288)))


newlines = linesplit(txt)
for newline in newlines:
    lineprint(newline)


