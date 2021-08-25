def temp_convert(c):
    return 9/5 * c + 32

def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m/1000

# f = temp_convert(34.6)
# print(f)
temp = [34.5,38.7,29.8,27.8,36.5,30.6]

# print(temp_convert(temp[0]))
# print(temp_convert(temp[1]))
# f = []
# for t in temp:
#     f.append(temp_convert(t))

# print(f)

kms = [122,231,500,65,23,6,8,12]
# ms = []
# for km in kms:
#     ms.append(km_to_m(km))

# print(ms)

# def my_map(func, iter):
#     data = []
#     for i in range(len(iter)):
#         data.append(func(iter[i]))
#     return data

# print(my_map(temp_convert, temp))
# print(my_map(km_to_m, kms))

print(list(map(temp_convert, temp)))
print(list(map(km_to_m, kms)))
