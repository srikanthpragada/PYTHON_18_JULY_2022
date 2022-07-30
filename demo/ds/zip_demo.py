l1 = [1, 2, 3, 4]
l2 = ['A', 'P', 'Q', 'Z']

for v1, v2 in zip(l1, l2, strict=True):
    print(v1, v2)
