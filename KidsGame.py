from random import randrange

x = True

while (x == True):
    ansNum = (randrange(10)+1)
    userAns = input("Guess a number between 1 and 10: ")
    guessNum = 1
    while(int(userAns) != ansNum):
        while (int(userAns) > 10 or int(userAns) < 1):
            userAns = input("Outside of range. Guess a number between 1 and 10: ")
            guessNum += 1
        if(int(userAns) < int(ansNum)):
            print("Too low.")
        if(int(userAns) > int(ansNum)):
            print("Too high.")
        if(int(userAns) != ansNum):
            userAns = input("Guess a number between 1 and 10: ")
            guessNum += 1

    print("Great job! The number was ",ansNum,". Guess count was ",guessNum,".")
    
    goAgain = input("Go again? (Y/N)")
    if(goAgain == "Yes" or goAgain == "yes" or goAgain == "Y" or goAgain == "y"):
        x = True
    else:
        x = False
        print("Thanks for playing.")