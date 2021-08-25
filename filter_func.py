def even(num):
    return num % 2 == 0

def odd(num):
    return num % 2 != 0

# print(even(45))
numbers = [4,6,7,3,12,4,7,9,0,34,78,9]
# e = []
# o = []
# for i in range(len(numbers)):
#     if even(numbers[i]):
#         e.append(numbers[i])
#
#     elif odd(numbers[i]):
#         o.append(numbers[i])
#
# print(e)
# print(o)

print(list(filter(even, numbers)))
print(list(filter(odd, numbers)))
