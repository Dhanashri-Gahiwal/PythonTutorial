import random

computerNumber = random.randint(1,10)

userNumber = int(input("Guess the number "))

if userNumber > computerNumber:
    print("Computer Number",computerNumber)
    print("OOPS! Your guess number is too high")

elif userNumber < computerNumber:
    print("Computer Number",computerNumber)
    print("OOPS! Your guess number is too low")

else:
    print("Computer Number",computerNumber)
    print("Congratulations!! Your guess number is equal")