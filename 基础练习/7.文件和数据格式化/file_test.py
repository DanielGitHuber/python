f = open('cwy_copy.txt', 'r')
for line in f:
    print(line)
f.seek(0)

print(f.read())
f.seek(0)

print(f.readlines())
f.close()
