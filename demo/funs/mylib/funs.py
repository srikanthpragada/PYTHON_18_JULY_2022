def iseven(n):
    return n % 2 == 0


def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False


# Run only when module is executed and not imported
if __name__ == '__main__':
    print(iseven(10), iseven(11))
