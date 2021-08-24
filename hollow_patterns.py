row = 6
for i in range(row):
    for j in range(row - i):
        print(' ', end='')
    for k in range(2*i + 1):
        if k == 0 or i == row - 1 or k == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
