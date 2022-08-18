class SavingsAccount:
    # static attribute or class attribute
    minbal = 10000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Balance")

    def get_balance(self):
        return self.balance

    def show(self):
        print(self.acno)
        print(self.ahname)
        print(self.balance)

    @property
    def available_balance(self):
        return self.balance - SavingsAccount.minbal


a1 = SavingsAccount(1, "Tom", 100000)  # __init__
print(a1.available_balance)
# print(SavingsAccount.minbal)
print(SavingsAccount.getminbal())  # calling static method
a1.withdraw(50000)
a1.show()
a2 = SavingsAccount(2, "David")
