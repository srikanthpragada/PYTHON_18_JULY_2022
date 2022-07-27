
s = "How Do You Do"

for c in s:
    code = ord(c)
    if code >= 65 and code <= 90:   # c.isupper()
        print(c)

