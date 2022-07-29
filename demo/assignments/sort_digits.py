num = 23423261

digits = []
while num > 0:
    digits.append(str(num % 10))
    num = num // 10

print("".join(sorted(digits)))
