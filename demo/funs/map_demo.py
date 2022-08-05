def digits(st):
    r = ""
    for c in st:
        if c.isdigit():
            r = r + c

    return r

names = ['java 18', 'c', 'python 10']

for l in map(len, names):
    print(l)

for s in map(digits, names):
    print(s)



