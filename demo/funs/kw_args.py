def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def showall(*args, **kwargs):
    print(args)
    print(kwargs)


show(x=10, y=20, a='abc')
showall(10, 20, x=1, y=100)
