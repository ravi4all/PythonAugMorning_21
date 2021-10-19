# x = 6
# y = 7
def calc_1():
    x = 6
    y = 7
    def add():
        z1 = x + y
        return z1
    def sub():
        z2 = x - y
        return z2
    # print(add(), sub())
    return add, sub

add, sub = calc_1()
print(add())
print(sub())
