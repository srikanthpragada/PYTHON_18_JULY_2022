def largest_string_by_length(*args):
    ll = 0
    for s in args:
        if len(s) > ll:
            ls = s
            ll = len(s)

    return ls


print(largest_string_by_length('abc', 'defg', 'zy', 'pqr'))
print(largest_string_by_length('abc', 'defg', 'abcd'))

