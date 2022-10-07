from random import randrange

# Text Based Game


# Player Stats

playerLVL = 1
playerHP = 100
playerHPCAP = playerHP
playerATK = 10
playerEXP = 0
playerCHC = ""


# Enemy Stats

enemyLVL = 1
enemyHP = 100
enemyATK = 10
enemyEXP = 0


# Environment Details

roomNUM = 1
roomSIZ = 10
roomCAP = 1
goFISRT = randrange(100)


# Player Action Functions

def action_choice(action, php, phpc, pha, ehp):
    if action == "Heal" or action == "heal":
        php += 10
        if php > phpc:
            php = phpc
            print("HP is at max.")
        return php
    elif action == "Attack" or action == "attack":
        ehp -= (pha % randrange(100)+1)
        return ehp


# Game Run

while(int(playerHP) > 0):
    print("You enter room number: ", roomNUM)
    print("You see ", roomCAP, " enemies in the room.")
    print("Player HP: ", playerHP)
    print("EnemyHP: ", enemyHP, "\n")
    if goFISRT % 2 == 0:
        print("Player Goes \n")
        playerCHC = input("Actions: Attack, Heal \n")
        if playerCHC == "Attack" or playerCHC == "attack":
            enemyHP = action_choice(playerCHC, playerHP, playerHPCAP, playerATK, enemyHP)
        elif playerCHC == "Heal" or playerCHC == "heal":
            playerHP = action_choice(playerCHC, playerHP, playerHPCAP, playerATK, enemyHP)
    else:
        for x in range(0, roomCAP):
            print("Enemy Goes \n")
            playerHP -= (enemyATK % randrange(100)+1)
    goFISRT += 1
    if enemyHP <= 0 and playerHP > 0:
        playerLVL += 1
        playerHPCAP += 50
        roomNUM += 1
        roomCAP += 1
    
print("Ended with: \n")
print("Player HP: ", playerHP)
print("Enemy HP: ", enemyHP)

    
    

