s = "Python"

codes = []
for c in s:
    codes.append(ord(c))

print(codes)

codes = [ord(c) for c in s]
print(codes)
