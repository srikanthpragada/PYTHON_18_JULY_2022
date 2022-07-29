st = "45,44,77,a,89,23"

total = 0
for p in st.split(","):
    if p.isdigit():
        total += int(p)

print(total)
