import random

cpu = random.randint(1,100)
chances = 0
game = True
while game:
    guess = int(input("Enter the number : "))
    if cpu == guess:
        print("Congrats, You guessed the number...")
        game = False
    elif cpu > guess:
        print("You have guessed smaller number...")
    elif cpu < guess:
        print("You have guessed larger number...")
    else:
        print("Invalid Number")
    chances += 1

    if chances == 5:
        print("No more chances are left...You Lose")
        print("Number was ::",cpu)
        game = False
