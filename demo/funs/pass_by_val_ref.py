def inc(n):
    print(id(a))
    n = n + 1


def prepend(l, n):
    l.add(0, n)


a = 100
print(id(a))
inc(a)
print(a)

l = [1, 2, 3]
prepend(l, 10)
print(l)
