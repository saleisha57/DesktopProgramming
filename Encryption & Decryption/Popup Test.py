import ctypes

# Constants for the type of message box, and the inputs from the message box.
class MbConstants:
    MB_YESNO = 4
    IDYES = 6
    IDNO = 7

print("This program is designed to collect information, and store it in a file. Please fill out the information below.")

# Gathering information from the user and storing in a dictionary.
user_info = {"FirstName":input("Enter your first name: "),
            "LastName":input("Enter your last name: "),
            "Age":input("How old are you: "),
            "Occupation":input("Enter your occupation: ")}


# Display the information the user entered.
# Display a promt for the user to choose yes or no to save their information to a file.
def file_save(ui):
    print()
    print("The information you entered is displayed below.\n")
    
    print(ui["FirstName"])
    print(ui["LastName"])
    print(ui["Age"])
    print(ui["Occupation"])
    
    KeyIn = input("Press Enter to continue...")
    
    if KeyIn == "":
        # Display the prompt window to the user.
        userIn = ctypes.windll.user32.MessageBoxW(0, "Do you want to save your information to a file?", "File Save Promt", MbConstants.MB_YESNO)
        
        #Check if the user cicked yes.
        if userIn == MbConstants.IDYES:
            # Ask the user for a file name and save the file with the infrmation.
            file_name = input("Enter a filename: ")
            user_file = open(file_name, "w")
            user_file.write("First Name: " + ui["FirstName"] + "\nLast Name: " + ui["LastName"] + "\nAge: " + ui["Age"] + "\nOccurpation: " + ui["Occupation"])
            user_file.close()
            print("Your file was saved...")
            return
        
        #Check if the user clicked no
        if userIn == MbConstants.IDNO:
            print("You did not save the file...")
            return    
    return


file_save(user_info)