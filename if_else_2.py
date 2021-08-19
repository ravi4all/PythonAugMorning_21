#If Else Ladder
num = int(input("Enter a number : "))

'''
if num % 2 == 0:
    print("Number is Even")
elif num % 2 != 0:
    print("Number is Odd")
else:
    print("Invalid Input...")
'''

#If Else Expression
result = "Even" if num % 2 == 0 else "Odd" if num %2 != 0 else "Invalid"
print("Result is",result)
