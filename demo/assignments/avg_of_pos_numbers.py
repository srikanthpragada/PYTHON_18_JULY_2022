# Display avg of positive numbers
total = count = 0
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break  # Terminate loop

    if num > 0:
        total += num
        count += 1

print(total // count)
