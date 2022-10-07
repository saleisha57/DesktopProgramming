 #Encryption through permutations of size 4 for now (Will include user input for the permutations)

#Asking the user for a sentence and the permutation key.
to_enc = input("Please enter a sentence to be encrypted: ")
key = input("Please enter key for a permutation of 4 (between 0 and 3): ")
checking = True

#Checking the length of the key.
while checking:
    while len(key) > 4 or len(key) == 0:
        key = input("Please enter key for a permutation of 4 (between 0 and 3): ")
    checking = False
   
checking = True

userkey = list(key)

#Checking the values in the key.
while checking:
    for x in range(len(key)):
        while userkey[x] < str(0) or userkey[x] > str(3):
            userkey[x] = input(key[x] + " is not in the range. Please enter a value between 0 and 3: ")
    checking = False

to_enc = list(to_enc)

#Perform the permutation
def Encryption(st, uk):
    holder = []
    for x in st:
        for i in range(0,len(x)):
            print(i)
            #holder.append(st[i])
        #for 
    return holder

#Add additional blank characters to the list if it is not divisible by the permutation length.
def Add_to_enc(te):    
    while len(te) % 4 != 0:
        te.append(' ')
    return te
    
#Break up the list into groups of the size of the permutation.
def Break_to_enc(enc):
    list = [enc[x:x+4] for x in range(0, len(enc), 4)]
    return list

morenc = Add_to_enc(to_enc)
newenc = Break_to_enc(morenc)
permu = Encryption(newenc, userkey)

print()
#print(morenc)
#print(newenc)
print(permu)
