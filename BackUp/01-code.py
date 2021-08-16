a = 12
b = 8
c = a + b
print(c)
print("Sum is",c)

print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {2} and {1} is {0}".format(c,b,a))

#f-strings - fast strings
print(f"Sum of {a} and {b} is {c}")
print(f"Sum of {a = } and {b = } is {c = }")

# Multi-line Print
'''
print("1. Add")
print("2. Sub")
print("3. Div")
print("4. Mul")

print("1. Add\n2. Sub\n3. Div\n4. Mul")
'''

print("""
      1. Add
      2. Sub
      3. Mul
      4. Div""")






