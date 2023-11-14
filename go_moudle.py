def hello(*names):
    for name in names:
        print('hello, ' + name)


def greet(names):
    for name in names:
        print('hello, ' + name.title())