l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30]

for idx, v1 in enumerate(l1):
    v2 = l2[idx] if idx < len(l2) else '*'
    print(v1, v2)
