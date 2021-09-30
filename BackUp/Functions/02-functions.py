# positional args
def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

# add(5,7)
# add(3,8)
# add(8,6)
# add(4,2)

def calc_1():
    num_1 = int(input("Enter first num : "))
    num_2 = int(input("Enter second num : "))
    # add(num_1, num_2)
    sub(num_1, num_2)

calc_1()