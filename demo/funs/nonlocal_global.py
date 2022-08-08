def f1():
    v1 = 10

    def f2():
        nonlocal v1
        v1 = 20
        print(v1)

    f2()
    print(v1)


f1()
