
class Movie:
    def __init__(self, p_title, p_year, p_rating, p_genre):
        self.title = p_title
        self.year = p_year
        self.rating = p_rating
        self.genre = p_genre

    def display_movie(self):
        print("\nTitle: " + self.title + "\nYear: " + self.year + "\nRating: " + self.rating + " out of 5 \nGenre: " + self.genre + "\n")



class Movielist:
    def __init__(self):
        self.movie_list = []


    def list_movies(self):
        print()
        if len(self.movie_list) == 0:
            print("Movie list is empty.")
        else:
            for entry in self.movie_list:
                print("Title: " + entry["Title"] + "\nYear: " + entry["Year"] + "\nRating: " + entry["Rating"] + " out of 5 \nGenre: " + entry["Genre"] + "\n")
        print()


    # Function for adding movies to the list.
    def add_movies(self):
        title = input("Enter the title of the movie.\n")
        year = input("Enter the year for the movie.\n")
        while (len(year)>4 or len(year)<4) or year.isalpha() or (not float(year).is_integer()):
            print("\nInvalid year. Try again.\n")
            year = input("Enter the year for the movie.\n")
        rating = input("Enter an integer between 1 and 5 for the rating.\n")
        while rating.isalpha() or (not float(rating).is_integer()) or (int(rating) < 1 or int(rating) > 5):
            print("Invalid rating. Try again.")
            rating = input("Enter an integer between 1 and 5 for the rating.\n")
        genre = input("Enter the genre for the movie.\n")
        print()

        movie_entry = Movie(title,year,rating,genre)
        movie_dictionary = {"Title": movie_entry.title, "Year": movie_entry.year, "Rating": movie_entry.rating, "Genre": movie_entry.genre}
        self.movie_list.append(movie_dictionary)
        

    # Function for deleting movies.
    def delete_movies(self):
         print ("\nCurrent movie list")
         self.list_movies()
         title_to_delete = input("Enter the title of the movie you would like to delete.\n")

         for iterator in range(0, len(self.movie_list)):
             if self.movie_list[iterator]["Title"] == title_to_delete:
                 print("\n" + title_to_delete + " has been removed.\n")
                 self.movie_list.pop(iterator)
         return self.movie_list


    #Function for editing movies in the list.
    def edit_movies(self):
        while True:
            user_choice = input("\nCOMMAND MENU \nWhat do you want to edit? \nEnter a integer between 1 and 5. \n1) Title \n2) Year \n3) Rating \n4) Genre \n5) Return with no changes\n")
            while user_choice.isalpha() or (not float(user_choice).is_integer()) or (int(user_choice) > 5 or int(user_choice) < 1):
                print("\nInvalid input. Try again.")
                user_choice = input("\nCOMMAND MENU \nWhat do you want to edit? \nEnter a integer between 1 and 5. \n1) Title \n2) Year \n3) Rating \n4) Genre \n5) Return with no changes\n")
            #Function for editing movie title.
            if int(user_choice) == 1:
                print("Current Movie List")
                self.list_movies()
                
                title_to_change = input("What is the current title of the movie you would like to update?\n")
                for iterator in range(0,len(self.movie_list)):
                    if self.movie_list[iterator]["Title"] == title_to_change:
                        new_title = input("Enter the new title.\n")
                        
                        while True:
                            print("Changing " + self.movie_list[iterator]["Title"] + " to " + new_title)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.movie_list[iterator]["Title"] = new_title 
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            #Function for editing movie year.            
            elif int(user_choice) == 2:
                print("Current Movie List")
                self.list_movies()
                
                year_to_change = input("What is the current title of the movie you would like to update?\n")
                for iterator in range(0,len(self.movie_list)):
                    if self.movie_list[iterator]["Title"] == year_to_change:
                        new_year = input("Enter the new year.\n")
                        while (len(new_year)>4 or len(new_year)<4) or new_year.isalpha() or (not float(new_year).is_integer()):
                            print("\nInvalid year. Try again.\n")
                            new_year = input("Enter the new year for the movie.\n")
                        while True:
                            print("Changing " + self.movie_list[iterator]["Year"] + " to " + new_year)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.movie_list[iterator]["Year"] = new_year
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            #Function for editing movie rating.       
            elif int(user_choice) == 3:
                print("Current Movie List")
                self.list_movies()
                
                rate_to_change = input("What is the current title of the movie you would like to update?\n")
                for iterator in range(0,len(self.movie_list)):
                    if self.movie_list[iterator]["Title"] == rate_to_change:
                        new_rate = input("Enter the new rating between 1 and 5.\n")
                        while new_rate.isalpha() or (not float(new_rate).is_integer()) or (int(new_rate) > 5 or int(new_rate) < 1):
                            print("Invalid rating. Try again.")
                            new_rate = input("Enter the new rating between 1 and 5.\n")
                            
                        
                        while True:
                            print("Changing " + self.movie_list[iterator]["Rating"] + " to " + new_rate)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.movie_list[iterator]["Rating"] = new_rate
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            #Function for editing movie genre.            
            elif int(user_choice) == 4:
                print("Current Movie List")
                self.list_movies()
                
                genre_to_change = input("What is the current title of the movie you would like to update?\n")
                for iterator in range(0,len(self.movie_list)):
                    if self.movie_list[iterator]["Title"] == genre_to_change:
                        new_genre = input("Enter the new genre.\n")
                        
                        while True:
                            print("Changing " + self.movie_list[iterator]["Genre"] + " to " + new_genre)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.movie_list[iterator]["Genre"] = new_genre
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            #Function for returning the user the the prior menu.            
            elif int(user_choice) == 5:
                return self.movie_list

        return self.movie_list




# Function for running the base program and main menu.
def run_program():
    movies = Movielist()
    
    while True:
        user_input = input("\nCOMMAND MENU \nEnter a integer between 1 and 5. \n1) List Movies \n2) Add Movies \n3) Delete Movies \n4) Edit Movies \n5) Exit Program\n")
        # Loop checking for valid input.
        while user_input.isalpha() or (not float(user_input).is_integer()) or (int(user_input) < 1 or int(user_input) > 5):
            print("\nNot a valid selection. Try again.\n")
            user_input = input("\nCOMMAND MENU \nEnter a integer between 1 and 5. \n1) List Movies \n2) Add Movies \n3) Delete Movies \n4) Edit Movies \n5) Exit Program\n")
                 
        if 1 <= int(user_input) or int(user_input) <= 5:
            if int(user_input) == 1:
                movies.list_movies()
            elif int(user_input) == 2:
                movies.add_movies()
            elif int(user_input) == 3:
                movies.delete_movies()
            elif int(user_input) == 4:
                movies.edit_movies()
            elif int(user_input) == 5:
                break


run_program()

