names = ['java', 'python', 'ruby', 'Sql']

for n in sorted(names, key=len):
    print(n)

for n in sorted(names, key=str.upper):  # case insensitive sorting
    print(n)
