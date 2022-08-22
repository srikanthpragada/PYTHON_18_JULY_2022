s = "0"
try:
    v = int(s)
    print(100 / v)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Number cannot be zero!")

print("The End")

