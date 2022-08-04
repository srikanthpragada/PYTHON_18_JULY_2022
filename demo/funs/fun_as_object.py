a = 10


def f1():
    print('f1')


f2 = f1
f1()
f2()

print(id(a), id(f1))
