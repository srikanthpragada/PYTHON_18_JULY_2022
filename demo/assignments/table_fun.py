def table(num, length=20):
    for i in range(1, length + 1):
        print(f"{num:3} * {i:2} = {num * i:5}")


table(25, 10)
table(15)
