names = ['Larry', 'Joe', 'Jack', 'Mike', 'Mike', 'Andy', 'Joe']

names_count = {}

for n in names:
    count = names_count.get(n, 0)
    names_count[n] = count + 1

print(names_count)

