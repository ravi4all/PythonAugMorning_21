import random

positions = [i+1 for i in range(9)]
occupied = []

def gameBoard():
    print("""
    {} | {} | {}
    -----------
    {} | {} | {}
    -----------
    {} | {} | {}
    """.format(positions[0], positions[1], positions[2],
           positions[3], positions[4], positions[5],
           positions[6], positions[7], positions[8]))

def checkWinner():
    pass

def userMove(ch):
    pos = int(input("Enter you position : "))
    positions[pos-1] = ch
    occupied.append(pos)

def cpuMove(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        print("Already Occupied",pos)
        cpuMove(ch)
    else:
        print("CPU Picked",(pos))
        positions[pos - 1] = ch
        occupied.append(pos)

def main():
    gameBoard()

    user_ch = input("Enter your choice : 0 or X : ")
    if user_ch == "0":
        cpu_ch = "X"
    else:
        cpu_ch = "0"

    while True:
        userMove(user_ch)
        gameBoard()
        cpuMove(cpu_ch)
        gameBoard()

main()