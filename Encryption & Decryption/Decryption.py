# Decryption

key = input("Enter the key for the decryption: ")
encMessage = input("Enter the string to decrypt: ")

brokenText = []
holderText = []

for x in range(len(encMessage)):
    holderText.append(encMessage[x])

while(holderText[:-(len(holderText)%4)]):
    holderText.append(' ')

while len(holderText) != 0:
    brokenText.append(holderText[0:4])
    for x in range(0,4):
        holderText.pop(0)

print(brokenText)

def decrypt(BT,K):
    holder = []
    keyHolder = [0,1,2,3]
    
    for i in range(len(K)):
        keyHolder.append(K[i])
    
    for x in BT:
        for i in range(0,4):
            if keyHolder[i] == K[i]:
                holder.append(BT[i])
        
    
    return holder


dec = decrypt(brokenText,key)

print('\n' + ''.join(dec))