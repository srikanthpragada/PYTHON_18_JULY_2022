class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("iPhone 13 Pro", 100000)
p2 = Product("iPhone 13 Pro", 100000)
print(p1)  # str(p1) -> p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
print(p1 > p2)  # p1.__gt__(p2)

prods = [Product('A', 10000), Product('B', 500), Product('C', 2000)]
for p in sorted(prods):
    print(p)
