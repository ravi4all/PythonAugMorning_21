import random

positions = [i+1 for i in range(9)]
occupied = []

winning_combinations = [
    [1,2,3], [4,5,6], [7,8,9],
    [1,4,7], [2,5,8], [3,6,9],
    [1,5,9], [3,5,7]
]

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

def checkWinner(ch, pos):
    for i in range(len(winning_combinations)):
        if pos in winning_combinations[i]:
            index = winning_combinations[i].index(pos)
            winning_combinations[i][index] = ch

    # print(winning_combinations)
    for i in range(len(winning_combinations)):
        if winning_combinations[i][0] == ch and winning_combinations[i][1] == ch and winning_combinations[i][2] == ch:
            print(ch,"Win...")
            return "win"

def userMove(ch):
    pos = int(input("Enter you position : "))
    positions[pos-1] = ch
    occupied.append(pos)
    return checkWinner(ch, pos)

def cpuMove(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        print("Already Occupied",pos)
        cpuMove(ch)
    else:
        print("CPU Picked",(pos))
        positions[pos - 1] = ch
        occupied.append(pos)
        return checkWinner(ch, pos)

def main():
    gameBoard()

    user_ch = input("Enter your choice : 0 or X : ")
    if user_ch == "0":
        cpu_ch = "X"
    else:
        cpu_ch = "0"

    while True:
        msg = userMove(user_ch)
        gameBoard()
        if msg == "win":
            break

        msg = cpuMove(cpu_ch)
        gameBoard()
        if msg == "win":
            break

main()