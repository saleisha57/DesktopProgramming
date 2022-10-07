# D&D Dice

from random import randrange

go_again = True

while(go_again):
    dice_type = input("Enter a Dice type from the follow: 20, 12, 10, 8, 6, 4 \n")
       
    # 20 Sided
    if(dice_type == "20"):
        roll = randrange(20)
        while(roll < 1 or roll > 20):
            roll = randrange(20)
        print("Dice Roll: ", roll)
    
    # 12 Sided
    if(dice_type == "12"):
        roll = randrange(12)
        while(roll < 1 or roll > 12):
            roll = randrange(12)
        print("Dice Roll: ", roll)
        
    # 10 Sided
    if(dice_type == "10"):
        roll = randrange(10)
        while(roll < 1 or roll > 10):
            roll = randrange(10)
        print("Dice Roll: ", roll)
        
    # 8 Sided
    if(dice_type == "8"):
        roll = randrange(8)
        while(roll < 1 or roll > 8):
            roll = randrange(8)
        print("Dice Roll: ", roll)
        
    # 6 Sided
    if(dice_type == "6"):
        roll = randrange(6)
        while(roll < 1 or roll > 6):
            roll = randrange(6)
        print("Dice Roll: ", roll)
        
    # 4 Sided
    if(dice_type == "4"):
        roll = randrange(4)
        while(roll < 1 or roll > 4):
            roll = randrange(4)
        print("Dice Roll: ", roll)
    
    user_in = input("Keep rolling? (Y/N) \n")
    if(user_in == "Y" or user_in == "y"):
        go_again = True
    else:
        go_again = False