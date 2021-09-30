# variable length argument
def add(*x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    print("Sum is",sum)

x = [[4,5,7], [3,5,3]]

add(x[0][1],x[1][0])
add(3,4,6,7)
add(4,6,8,9,4,2)
add(1,2,5,7,8,5,6,9,7,5,4,5,7)
