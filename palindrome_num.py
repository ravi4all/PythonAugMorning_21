num = int(input("Enter a number : "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Number is palindrome...")
else:
    print("Number is not palindrome...")
