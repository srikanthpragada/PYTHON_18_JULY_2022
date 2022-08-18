class Counter:
    count = 0

    @staticmethod
    def get_count():
        return Counter.count

    def __init__(self, value=0):
        self.value = value
        Counter.count += 1

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value


c = Counter(10)
c2 = Counter()
print(Counter.get_count())

c.increment()
c.increment()
print(c.get_value())
