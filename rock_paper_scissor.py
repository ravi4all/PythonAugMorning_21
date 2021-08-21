import random

operations = ["rock","paper","scissor"]

user_score = 0
cpu_score = 0
count = 0

game = True
while game:
    cpu = random.choice(operations)
    user = input("Enter your choice : ")
    if user == cpu:
        print("Tie...")
    elif user == "rock" and cpu == "paper":
        print("Cpu Win...")
        cpu_score += 1
    elif user == "paper" and cpu == "scissor":
        print("Cpu Win...")
        cpu_score += 1
    elif user == "scissor" and cpu == "rock":
        print("Cpu Win...")
        cpu_score += 1
    elif user == "rock" and cpu == "scissor":
        print("User Win...")
        user_score += 1
    elif user == "paper" and cpu == "rock":
        print("User Win...")
        user_score += 1
    elif user == "scissor" and cpu == "paper":
        print("User Win...")
        user_score += 1
    print("CPU ::",cpu)
    count += 1

    if count == 5:
        game = False

if user_score > cpu_score:
    print("User win")
else:
    print("CPU Win")
    
