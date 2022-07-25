# Common Factors
num1 = 255
num2 = 124

small_num = num1 if num1 < num2 else num2

for i in range(2, small_num // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i, end=' ')
