from math import sqrt


s = []
for i in range(2, 201):
    k = True
    for j in range(2, i):
        if i % j == 0:
            k = False
            break
    if k:
        s.append(i)
print(s, '\n')

s = []
for i in range(2, 201):
    k = True
    for j in range(2, int(sqrt(i))+1):  # or int(i/2)+1
        if i % j == 0:
            k = False
            break
    if k:
        s.append(i)
print(s, '\n')



