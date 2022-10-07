# Encryption using permutations

# Ask the user for the key they want to encrypt based on.
key = input("Enter the encryption key with numbers between 0 and 3 in any order: ")

# Ask the user for the sentence to encrypt.
plainText = input("Enter the sentence you would like to encrypt: ")

# Lists for breaking apart the user input.
brokenText = []
holderText = []

# Breaks the sentence into lists.
for x in range(len(plainText)):
    holderText.append(plainText[x])

# Append spaces to text for transposition.
while(holderText[:-(len(holderText)%4)]):
    holderText.append(' ')

# Add for the groups of 4 to encrypt.
while len(holderText) != 0:
    brokenText.append(holderText[0:4])
    for x in range(0,4):
        holderText.pop(0)

# Perform the encryption using permutations.
def encrypt(BT, K):
    holderList = []
    keyHolder = []
    
    # Convert user input key into a list for easy iteration.
    for i in range(len(K)):
        keyHolder.append(K[i])
    
    # Encrypt based on the user input key.
    for x in range(0,len(BT)):
        for i in range(0,4):
            holderList.append(BT[x][int(keyHolder[i])])
    
    return holderList


enc = encrypt(brokenText, key)

# Print the outcome.
print('\n' + ''.join(enc))


