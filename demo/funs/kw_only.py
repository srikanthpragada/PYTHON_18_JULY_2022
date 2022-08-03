# Keyword-only params
def wish(*, user, message="Hi"):
    print(message, user)


wish(user="Andy", message="Hello")
# wish("Bill")
