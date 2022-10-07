# Music Library

songs = []
loop = True

# Display songs in list.
def showSongs(listIn):
    print()
    for entry in listIn:
        print(entry["Title"] + " by " + entry["Artist"] + " - " + entry["Year"] + " (" + entry["Genre"] + ")")
    print()


# Add a song to the list.
def addSongs(listIn):
    songTitle = input("\nEnter the song title.\n")
    artist = input("Enter the artist.\n")
    year = input("Enter the year.\n")
    genre = input("Enter the genre.\n")
    
    entry = {"Title":songTitle, "Artist":artist, "Year":year, "Genre":genre}
    listIn.append(entry)
    return listIn

# Remove a song from the list.
def delSongs(listIn):
    songRem = input("\nEnter the title of the song to remove.\n")
    
    for i in range(0, len(listIn)):
        if listIn[i]["Title"] == songRem:
            listIn.pop(i)
    return listIn


# Edit a song in the list.
def editSongs(listIn):    
    while True:
        userChoice = input("\nWhich would you like to update? \n1) Title \n2) Artist \n3) Year \n4) Genre \n5) None \n")
        
        if int(userChoice) == 1:
            songUpdate = input("\nWhich song title would you like to update?\n")
            artistUpdate = input("What is the current artist of this song?\n")
            for i in range(0, len(listIn)):
                if listIn[i]["Title"] == songUpdate and listIn[i]["Artist"] == artistUpdate:
                    newTitle = input("What song title would you like?\n")
                    listIn[i]["Title"] = newTitle
        elif int(userChoice) == 2:
            artistUpdate = input("\nWhich artist would you like to update?\n")
            songUpdate = input("What is the current song entry for this artist?\n")
            for i in range(0, len(listIn)):
                if listIn[i]["Title"] == songUpdate and listIn[i]["Artist"] == artistUpdate:
                    newArtist = input("What artist would you like?\n")
                    listIn[i]["Artist"] = newArtist
        elif int(userChoice) == 3:
            artistUpdate = input("\nWhat is the artist for the year would you like to update?\n")
            songUpdate = input("What is the current song entry for this artist?\n")
            for i in range(0, len(listIn)):
                if listIn[i]["Title"] == songUpdate and listIn[i]["Artist"] == artistUpdate:
                    newYear = input("What year would you like?\n")
                    listIn[i]["Year"] = newYear
        elif int(userChoice) == 4:
            artistUpdate = input("\nWhich artist for the genre would you like to update?\n")
            songUpdate = input("What is the current song entry for this artist?\n")
            for i in range(0, len(listIn)):
                if listIn[i]["Title"] == songUpdate and listIn[i]["Artist"] == artistUpdate:
                    newGenre = input("What genre would you like?\n")
                    listIn[i]["Genre"] = newGenre
        else:
            return listIn
    
    return listIn



while loop:
    userInput = input("\nWhat would you like to do? \n1) View Song List \n2) Add a Song \n3) Delete a Song \n4) Edit a Song \n5) Exit \n")
    if int(userInput) == 1:
        showSongs(songs)
    elif int(userInput) == 2:
        songs = addSongs(songs)
    elif int(userInput) == 3:
        songs = delSongs(songs)
    elif int(userInput) == 4:
        songs = editSongs(songs)
    elif int(userInput) == 5:
        loop = False
    