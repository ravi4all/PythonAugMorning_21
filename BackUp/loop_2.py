'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
'''

num = int(input("Enter a num : "))

for i in range(1,11):
    print("{} x {} = {}".format(num, i, num * i))
