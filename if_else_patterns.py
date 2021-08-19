for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print("1",end='')
        else:
            print("0",end='')
    print()

print("*" * 30)
k = 0
for i in range(5):
    for j in range(5):
        k += 1
        if k % 2 == 0:
            print("0", end='')
        else:
            print("1", end='')
    print()
