# Positional-only params
def wish(user, message="Hi", /):
    print(message, user)


wish("Bill", "Hello")
# wish(user="Andy")
