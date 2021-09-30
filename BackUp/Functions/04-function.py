# positional + default
def add(x, y, z=6):
    z1 = x + y
    z2 = z + z1
    print(z1, z2)

add(4,5)
add(4,5,9)
