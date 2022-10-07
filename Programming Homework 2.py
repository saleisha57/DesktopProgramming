# Movie List Program

# 
def list_movies(movie_list):
    print()
    for entry in movie_list:
        print("Title: " + entry["Title"] + "\nYear: " + entry["Year"] + "\nRating: " + entry["Rating"] + " out of 5 \nGenre: " + entry["Genre"] + "\n")
    print()

#
def add_movies(movie_list):
    title = input("Enter the title of the movie.\n")
    year = input("Enter the year for the movie.\n")
    rating = input("Enter an integer between 1 and 5 for the rating.\n")
    while rating.isalpha() or (not float(rating).is_integer()) or (int(rating) < 1 or int(rating) > 5):
        print("Invalid selection. Try again.")
        rating = input("Enter an integer between 1 and 5 for the rating.\n")
    genre = input("Enter the genre for the movie.\n")
    print()
    
    movie_dictionary = {"Title":title, "Year":year, "Rating":rating, "Genre":genre}
    movie_list.append(movie_dictionary)
    
    return movie_list
    
    
#
def delete_movies(movie_list):
    title_to_delete = input("Enter the title of the movie you would like to delete.\n")
    
    for iterator in range(0, len(movie_list)):
        if movie_list[iterator]["Title"] == title_to_delete:
            print("\n" + title_to_delete + " has been removed.\n")
            movie_list.pop(iterator)
    return movie_list
    

#
def edit_movies(movie_list):
    while True:
        user_choice = input("COMMAND MENU \nWhat do you want to edit? \nEnter a integer between 1 and 5. \n1) Title \n2) Year \n3) Rating \n4) Genre \n5) Return with no changes\n")
        while user_choice.isalpha() or (not float(user_choice).is_integer()) or (int(user_choice) > 5 or int(user_choice) < 1):
            print("Invalid input. Try again.")
            user_choice = input("Enter the new rating between 1 and 5.\n")
        
        if int(user_choice) == 1:
            print("Current Movie List")
            list_movies(movie_list)
            
            title_to_change = input("What is the current title of the movie you would like to update?\n")
            for iterator in range(0,len(movie_list)):
                if movie_list[iterator]["Title"] == title_to_change:
                    new_title = input("Enter the new title.\n")
                    
                    while True:
                        print("Changing " + movie_list[iterator]["Title"] + " to " + new_title)
                        confirmation = input("Are you sure? (Yes or No)\n")
                        
                        if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                            movie_list[iterator]["Title"] = new_title 
                            break
                        elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                            break
                        else:
                            print("Not a valid selection. Try again.")
                    
        elif int(user_choice) == 2:
            print("Current Movie List")
            list_movies(movie_list)
            
            year_to_change = input("What is the current title of the movie you would like to update?\n")
            for iterator in range(0,len(movie_list)):
                if movie_list[iterator]["Title"] == year_to_change:
                    new_year = input("Enter the new year.\n")
                    
                    while True:
                        print("Changing " + movie_list[iterator]["Year"] + " to " + new_year)
                        confirmation = input("Are you sure? (Yes or No)\n")
                        
                        if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                            movie_list[iterator]["Year"] = new_year
                            break
                        elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                            break
                        else:
                            print("Not a valid selection. Try again.")
                    
        elif int(user_choice) == 3:
            print("Current Movie List")
            list_movies(movie_list)
            
            rate_to_change = input("What is the current title of the movie you would like to update?\n")
            for iterator in range(0,len(movie_list)):
                if movie_list[iterator]["Title"] == rate_to_change:
                    new_rate = input("Enter the new rating between 1 and 5.\n")
                    while new_rate.isalpha() or (not float(new_rate).is_integer()) or (int(new_rate) > 5 or int(new_rate) < 1):
                        print("Invalid input. Try again.")
                        new_rate = input("Enter the new rating between 1 and 5.\n")
                        
                    
                    while True:
                        print("Changing " + movie_list[iterator]["Rating"] + " to " + new_rate)
                        confirmation = input("Are you sure? (Yes or No)\n")
                        
                        if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                            movie_list[iterator]["Rating"] = new_rate
                            break
                        elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                            break
                        else:
                            print("Not a valid selection. Try again.")
                    
        elif int(user_choice) == 4:
            print("Current Movie List")
            list_movies(movie_list)
            
            genre_to_change = input("What is the current title of the movie you would like to update?\n")
            for iterator in range(0,len(movie_list)):
                if movie_list[iterator]["Title"] == genre_to_change:
                    new_genre = input("Enter the new genre.\n")
                    
                    while True:
                        print("Changing " + movie_list[iterator]["Genre"] + " to " + new_genre)
                        confirmation = input("Are you sure? (Yes or No)\n")
                        
                        if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                            movie_list[iterator]["Genre"] = new_genre
                            break
                        elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                            break
                        else:
                            print("Not a valid selection. Try again.")
                    
        elif int(user_choice) == 5:
            return movie_list
    
    return movie_list


#
def run_program():
    movie_list = []
    while True:
        user_input = input("\nCOMMAND MENU \nEnter a integer between 1 and 5. \n1) List Movies \n2) Add Movies \n3) Delete Movies \n4) Edit Movies \n5) Exit Program\n")
        
        while user_input.isalpha() or (not float(user_input).is_integer()) or (int(user_input) < 1 or int(user_input) > 5):
            print("\nNot a valid selection. Try again.\n")
            user_input = input("\nCOMMAND MENU \nEnter a integer between 1 and 5. \n1) List Movies \n2) Add Movies \n3) Delete Movies \n4) Edit Movies \n5) Exit Program\n")
                 
        if 1 <= int(user_input) or int(user_input) <= 5:
            if int(user_input) == 1:
                list_movies(movie_list)
            elif int(user_input) == 2:
                movie_list = add_movies(movie_list)
            elif int(user_input) == 3:
                movie_list = delete_movies(movie_list)
            elif int(user_input) == 4:
                movie_list = edit_movies(movie_list)
            elif int(user_input) == 5:
                break


run_program()

