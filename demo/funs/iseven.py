def iseven(n):
    return n % 2 == 0


def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def avg(*nums):
    total = sum(nums)
    return total / len(nums)


print(iseven(10), iseven(11))
print(isprime(13), isprime(1343434341))
print(avg(10,20,30,45))

