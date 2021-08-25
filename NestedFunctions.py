# Nested Functions

def calc():
    x = 6
    y = 7
    def add():
        nonlocal x
        x = 10
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add, sub


add, sub = calc()
print(add(),sub())


