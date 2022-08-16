class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # private attribute

    def get_age(self):
        return self.__age

p1 = Person("Larry", 35)
print(p1.__dict__)
#print(p1._Person__age)
print(p1.get_age())
