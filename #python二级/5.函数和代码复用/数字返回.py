import sys


def isNum():
    global a
    a = input('input a word(q&Q to exit):')
    try:
        while complex(a) or int(a) or float(a):
            return True
    except:
        return False


while True:
    print(isNum())
    if a == 'q' or a == 'Q':
        sys.exit()