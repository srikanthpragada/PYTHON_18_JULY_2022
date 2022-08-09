# Take number and length (optional) on command line and display
# table for the given number

import sys

if len(sys.argv) < 2:
    print("Number is missing!")
    exit()

if len(sys.argv) > 2:   # length is given
    length = int(sys.argv[2])
else:
    length = 10   # default length


num = int(sys.argv[1])
for i in range(1, length + 1):
    print(f"{num:3} * {i:2} = {i * num:5}")
