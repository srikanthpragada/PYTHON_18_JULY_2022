def count_lower_upper(st):
    lower = upper = 0
    for c in st:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1

    return lower, upper


print(count_lower_upper("Abc Xyz PQR"))
