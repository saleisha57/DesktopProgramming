#Random Code in Python

#Testing to see if I can get audio files to play.

class Song:
    def __init__(self, title, artist, year, genre, length):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre
        self.length = length

class Playlist:
    def __init__(self):
        self.song_list = []
    
    
    def print_playlist(self):
        print()
        for entry in self.song_list:
            print("\nTitle: " + entry["Title"] + "\nArtist: " + entry["Artist"] + "\nYear: " + entry["Year"] + "\nGenre: " + entry["Genre"] + "\nLength: " + entry["Length"])
    
    
    def add_songs(self):
        print("\n\nAdding a new song...\n\n")
        title = input("Enter the song title.\n")
        artist = input("Enter the song artist.\n")
        year = input("Enter the song year.\n")
        genre = input("Enter the song genre.\n")
        print("Enter the length of the song for this format (hour : minute : second)")
        hours = input("Hours: ")
        minutes = input("Minutes: ")
        seconds = input("Seconds: ")
        
        while (not float(hours).is_integer()) or (not float(minutes).is_integer()) or (not float(seconds).is_integer()):
            print("\n\nInvalid input, try again.\n\n")
            hours = input("Hours: ")
            minutes = input("Minutes: ")
            seconds = input("Seconds: ")
        
        length = hours + ":" + minutes + ":" + seconds 
        
        song = Song(title,artist,year,genre,length)
        
        new_song = {"Title":song.title, "Artist":song.artist, "Year":song.year, "Genre":song.genre, "Length":song.length}
        
        self.song_list.append(new_song)
        print("\n" + new_song["Title"]+ " was added to the playlist.\n\n")
    
    
    
    
    
    def organize_songs(self):
        user_input = input("How would you like to organize?\n 1)Alphabetically \n2) By Length \n3) By Artist\n\n")
        
        if(user_input.isalpha() or (not float(user_input).is_integer()) or (int(user_input) < 1 or int(user_input) > 5)):
            print("Entry not correct, try again.")
            user_input = input("How would you like to organize?\n 1)Alphabetically \n2) By Length \n3) By Artist")
            
            
        if int(user_input) == 1:
            self.sort_by_alphabet()








def do_work():
    play = Playlist()
    
    while True:
        user_input = input("Create / Modify a playlist? (y/n)")
        
        while (not (user_input == "y" or user_input == "Y" or user_input == "yes" or user_input == "Yes")) and (not(user_input == "n" or user_input == "N" or user_input == "no" or user_input == "No")):
            print("\n\nInvalid input, try again.")
            user_input = input("\nCreate / Modify a playlist? (y/n)\n")
        
        print("\n\nCreating playlist...\n\n")
        while (user_input == "y" or user_input == "Y" or user_input == "yes" or user_input == "Yes") or (user_input == "n" or user_input == "N" or user_input == "no" or user_input == "No"):
            number_of_songs = input("\nHow many songs would you like to add?\n")
            for x in range(0, int(number_of_songs)):
                play.add_songs() 
            play.print_playlist()
            
            
        


do_work()