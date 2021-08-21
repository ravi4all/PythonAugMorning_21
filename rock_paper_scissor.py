import random

operations = ["rock","paper","scissor"]

game = True
while game:
    cpu = random.choice(operations)
    user = input("Enter your choice : ")
    print("CPU ::",cpu)
    if user == cpu:
        print("Tie...")
    elif user == "rock" and cpu == "paper":
        print("Cpu Win...")
    elif user == "paper" and cpu == "scissor":
        print("Cpu Win...")
    elif user == "scissor" and cpu == "rock":
        print("Cpu Win...")
    elif user == "rock" and cpu == "scissor":
        print("User Win...")
    elif user == "paper" and cpu == "rock":
        print("User Win...")
    elif user == "scissor" and cpu == "paper":
        print("User Win...")
