def iseven(n):
    """
    Checks whether the given number is even.
    :param n: Number to check
    :return:  True if number is even, False otherwise
    """
    return n % 2 == 0


def has_upper(s):
    """
       Checks whether the given string has uppercase letter.
       :param n: String to check
       :return: True if string has uppercase letter, otherwise false
    """
    for c in s:
        if c.isupper():
            return True

    return False


# Run only when module is executed and not imported
if __name__ == '__main__':
    print(iseven(10), iseven(11))
