def wish(message, user):
    print(message, user)


wish("Hi", "Scott")  # Positional
wish(user="Kevin", message="Hello")  # Keyword args
wish("Hello", user="Ellison")  # mixed
