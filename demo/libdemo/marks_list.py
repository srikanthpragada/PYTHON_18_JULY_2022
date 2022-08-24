f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    #print(parts)
    name = parts[0]
    marks = [int(v) for v in parts[1:] if v.isdigit()]
    #print(marks)
    total = sum(marks)
    # total = sum(map(int, parts[1:]))
    print(f"{name:15}  {total:3}  {total/len(marks):5.2f}")

f.close()
