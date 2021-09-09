a = 6
b = 5
#walrus operator
#print("Sum is",c := a + b)

print(f"""
Sum is {(c := a + b)}
Sub is {(d := a - b)}
Div is {(e := a / b)}
Mul is {(f := a * b)}
""")
