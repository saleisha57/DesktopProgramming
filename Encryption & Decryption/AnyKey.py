# Encryption using permutations

# Ask the user for the key length
kLen = 'num'

while kLen.isalpha() or float(kLen).is_integer() == False or int(kLen) <= 0:
    kLen = input("Enter an integer for the length you want for the key: ")


# Ask the user for the key they want to encrypt based on.
key = input("Enter the encryption key with numbers between 0 and the key length minus 1 in any order in one grouping (i.e.: A key length of 4, Key: 2301): ")

#Ask the user for the sentence to encrypt.
plainText = input("Enter the sentence you would like to encrypt: ")

# Lists for breaking apart the user input.
brokenText = []
holderText = []

# Breaks the sentence into lists.
for x in range(len(plainText)):
    holderText.append(plainText[x])

# Append spaces to text for transposition.
while(holderText[:-(len(holderText)%int(kLen))]):
    holderText.append(' ')

# Add for the groups of 4 to encrypt.
while len(holderText) != 0:
    brokenText.append(holderText[0:int(kLen)])
    for x in range(0,int(kLen)):
        holderText.pop(0)

#Perform the encryption using permutations.
def encrypt(BT, K):
    holderList = []
    keyHolder = []
    
    # Convert user input key into a list for easy iteration.
    for i in range(len(K)):
        keyHolder.append(K[i])
    
    # Encrypt based on the user input key.
    for x in range(0,len(BT)):
        for i in range(0,int(kLen)):
            holderList.append(BT[x][int(keyHolder[i])])
    
    return holderList


enc = encrypt(brokenText, key)

# Print the outcome.
print('\n' + ''.join(enc))










