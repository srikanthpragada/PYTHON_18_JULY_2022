def inc(n):
    print(id(n))
    n = n + 1
    print(id(n))


def prepend(l, n):
    l.insert(0, n)


a = 100
print(id(a))
inc(a)
print(a)

l = [1, 2, 3]
prepend(l, 10)
print(l)
