nums = [10, 11, 18, 30, 45, 55]


def iseven(n):
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)


for c in filter(str.isupper, "AbcDef"):
    print(c)

for d in filter(str.isdigit, ["abc", "123", "def", "456"]):
    print(d)
