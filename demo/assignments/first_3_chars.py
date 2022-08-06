names = ['java', 'python', 'c', 'c#', 'typescript']


def first3(s):
    return s[:3]


for n in map(first3, names):
    print(n)

for n in map(lambda s: s[:3], names):
    print(n)
