# default args
def add(x=0, y=0):
    z = x + y
    print("Sum is",z)

# add()
# add(5)
# add(4,5)

# Keyword args
# add(x = 6, y = 7)
# add(y = 3, x = 7)

add()
add(5)
add(6,7)
add(y=7)
add(x=6)
add(x=5,y=8)

