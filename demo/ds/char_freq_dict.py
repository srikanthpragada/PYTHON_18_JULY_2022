st = "how do you do today"

cf = {}
for c in set(st):
    cf[c] = st.count(c)

for char, cnt in sorted(cf.items()):
    print(char, cnt)
