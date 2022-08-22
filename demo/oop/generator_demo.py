def numbers():
    for n in range(5):
        yield n


g = numbers()
print(g)
print(next(g))
print(next(g))
