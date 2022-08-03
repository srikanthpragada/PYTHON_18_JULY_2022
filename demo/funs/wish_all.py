def wish(*users, message="Hi"):
    for u in users:
        print(message, u)


wish("Mike", "Bill")
wish("Joe", "Jack", "Jason", message="Hello")
