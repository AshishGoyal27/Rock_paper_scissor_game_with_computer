from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

def more_round():
    a = input("Want to play more?(y/n)")
    if a == 'y' or a=='Y':
        player = False
        computer = t[randint(0,2)]
    elif a == 'n' or a == 'N':
        player = True
    else:
        print("That's not an valid option either write y for yes or n for no")
        more_round()
    return player

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        
    player = more_round()
    computer = t[randint(0,2)]
    
