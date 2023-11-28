from random import *
a = ['a', 'b', 'c', 'd']
seed(10)
print(random())
print(randint(1, 10))
print(getrandbits(10))
print(randrange(1, 10, 2))
print(uniform(1, 10))
print(choice(a))

shuffle(a)
print(a)

print(sample(a, 2))
