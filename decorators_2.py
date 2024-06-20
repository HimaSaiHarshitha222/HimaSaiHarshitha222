def decorator(wrapped):
    def inner():
        print("I got decorated")
        wrapped()
    return inner

def ordinary():
    print("I am an ordinary function")


pretty = decorator(ordinary)
pretty()
