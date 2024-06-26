import random

l = ["rock","paper","scissor"]

computerChoice = random.choice(l)
ccount = 0
ucount = 0

while True:
    inp = int(input('''
                    You want to play game?
                    1 Yes
                    2 No
                    '''))
    if(inp == 1):      
        for i in range(1,6):
            userChoice = input("Enter your choice, rock or paper or scissor ")

            if(userChoice == "rock" and computerChoice =="paper"):
                print("Computer choice",computerChoice)
                print("computer win")
                ccount += 1

            if(userChoice == "rock" and computerChoice =="scissor"):
                print("Computer choice",computerChoice)
                print("user win")
                ucount += 1

            if(userChoice == "paper" and computerChoice =="scissor"):
                print("Computer choice",computerChoice)
                print("computer win")
                ccount += 1

            if(userChoice == "paper" and computerChoice =="rock"):
                print("Computer choice",computerChoice)
                print("user win")
                ucount +=1

            if(userChoice == "scissor" and computerChoice =="rock"):
                print("Computer choice",computerChoice)
                print("computer win")
                ccount +=1

            if(userChoice == "scissor" and computerChoice =="paper"):
                print("Computer choice",computerChoice)
                print("user win")
                ucount +=1
            
            if(userChoice == computerChoice):
                print("Computer choice",computerChoice)
                print("draw the game")

        print("user count",ucount)
        print("computer count",ccount)

        if(ccount == ucount):
            print("Game is tie")
        elif(ccount > ucount):
            print("Computer is winner")
        else:
            print("User is winner")

        ccount = 0
        ucount = 0

    elif(inp == 2):
        break

    else:
        print("Enter valid choice")
