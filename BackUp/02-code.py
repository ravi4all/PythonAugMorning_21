#a = 10
#b = 20
#c = a + b

#walrus operator
#print("Sum is",c := a + b)

print(a := 10, b := 20, c := a+b)

print(f"Sum of {(a := 10)} and {(b := 20)} is {(c := a + b)}")
