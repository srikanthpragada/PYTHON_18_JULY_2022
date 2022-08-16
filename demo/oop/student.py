class Student:
    # constructor
    def __init__(self, admno, name, course='python'):
        # Object attributes
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    # Method
    def show(self):
        print(f"Admno   : {self.admno}")
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")
        print(f"Feepaid : {self.feepaid}")

    def payment(self, amount):
        self.feepaid = self.feepaid + amount

    def total_fee(self):
        if self.course == 'python':
            return 10000
        else:
            return  12000

    def due_amount(self):
        return self.total_fee() - self.feepaid


# Create an object of Student class
s1 = Student(1, 'Steve')
s1.course = "java"
print(s1.total_fee())
s1.payment(5000)
s1.payment(2000)
s1.show()
print(s1.due_amount())

s2 = Student(2, "Mark", 'java')
s2.show()
