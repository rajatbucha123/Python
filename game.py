import random

print("Welcome to the game")

print("Let start the game\n,snake,water,gun")

count = 0
Plsc= 0
Csc = 0
tie = 0

csw = ["snake","water","gun"]

while count <= 5:
    computer = random.choice(csw)
    print("*********Turn -",str(count+1),"*******")
    player = input("Enter the choice")
    if player == computer:
        print("tie")
    elif player == "snake":
        if computer == "gun":
            print("You lose!",computer)
            Plsc =Plsc - 1
            Csc = Csc + 1
        else:
            print("You Win!", player)
            Plsc = Plsc + 1
            Csc = Csc - 1
    elif player == "water":
        if computer == "snake":
            print("You loss!",computer)
            Plsc =Plsc - 1
            Csc = Csc + 1
        else:
            print("You Win!", player)
            Plsc = Plsc + 1
            Csc = Csc - 1
    elif player == "gun":
        if computer == "water":
            print("You loss!",computer)
            Plsc =Plsc - 1
            Csc = Csc + 1
        else:
            print("You Win!", player)
            Plsc = Plsc + 1
            Csc = Csc - 1
    else:
        print("INVALID Word")

computer = random.choice(csw)
count = count+1

if player == "win":
    Plsc = "score"
