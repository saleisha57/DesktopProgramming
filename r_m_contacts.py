import time
import datetime
import sys

#create the class
class contact:
    def __init__(self, p_first_name, p_last_name, p_age, p_phone, p_email, p_id_number):
        self.__id_number = p_id_number
        self.__first_name = p_first_name
        self.__last_name = p_last_name
        self.__age = p_age
        self.__email = p_email
        self.__phone = p_phone


#Getters Setters
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(p_first_name):
        self.__first_name = p_first_name
    
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(p_last_name):
        self.__last_name = p_last_name
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(p_age):
        self.__age = p_age

    @property
    def id_number(self):
        return self.__id_number

    @age.setter
    def id_number(p_age):
        self.__id_number = p_id_number  
    
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(p_phone):
        self.__phone = p_phone
    
    def clean_summary(self):
        return self.__first_name +" " + self.__last_name + "\n    Age: " + str(self.__age) + "\n    Phone: " + str(self.__phone) + "\n    Email: " + (self.__email)
#Here we create the contact list class and various functions inside.

class contact_list:
    def __init__(self):
        self.__contact_list = []
        self.__contact_list.append(contact(str("Test"), str("Dummy"), 18, 555-555-555, "whatever@email.com", 5))

    def get_user_choice(self,p_prompt = "Please enter a number greater or equal to 0: ", p_lower_Limit = 0, p_upper_Limit = 99999999999999):
        while True:
            try:
                user_input = int(input(p_prompt))
                if p_lower_Limit <= user_input <= p_upper_Limit:               #  Checking the range against parameters lower and upper limit
                    return user_input
                else:
                    print("Incorrect input: the number enetered was not a valid number. Please try again")
            except ValueError:
                print("Please input a number")    
    
    
    
    def length(self):
        return len(self.__contact_list)    
#Here we will be able to disply the contact list
    def print_contacts(self):
        if(self.length() ==0):
            input("contact list is currently empty, press enter to continue.")
            return
        contact_id_num = 0
        for individual_contact in self.__contact_list:
            contact_id_num += 1
            print(str(individual_contact) + " , " + individual_contact.clean_summary())

#Here we will create our contacts
    def add_contact(self):
        self.__contact_list.append(self.new_contact())
#Creating the new contact
    def new_contact(self):
        new_id = input("Contact ID: ")
        new_first_name = input("First name for contact: ")
        new_last_name = input("Last name for contact: ")
        new_age = input("Age of  contact: ")
        new_phone_num = input("Phone for contact: ")
        new_email_acc = input("Email for contact: ")
        return contact(new_first_name, new_last_name, new_age, new_phone_num, new_email_acc, new_id)

#Setting the position for contact
    def get_contact_position(self, p_first_name):
        position = 0
        for contact in self.__contact_list:
            if contact.first_name == p_first_name:
                return position
            position += 1
        return -1
#Editing contacts from our list
    def edit_contact(self):
        if(self.length() == 0):
            print("Contact list looking empty")
            input("Please enter to continue..")
            return
        else:
            user_selection = self.get_user_choice(1, self.length(), "Enter the contact you wish to edit: ")
            self.__contact_list[user_selection - 1] = self.new_contact()    

# Here we delete the contacts
    def delete_contact(self):
        user_choice = get_user_choice("Enter ID number of the contact you wish to delete: ")
        try:
            contact_position = self.get_contact_position(user_choice)
            if contact_position >= 0:
                self.__contact_list.pop(contact_position)
            else:
                print("Doesnt look like thats available try again?: ")
        except:
            print("\n .:.Invalid contact information.:.")
            input("\nPress Enter to continue...")


#We exit the class and begin a few extra functions here for get char.
def get_character(self,p_prompt = "Please enter your choice: [a or d or e or l or q | Or type the word]: ", allowed_characters = 'AabBcCdDeEfFgGhHiIjJkKLlmMnNoOpPqQrRsStTuUvVwWxXyZ'):
        allowed_strings = ['delete','edit','add','list','quit']  ## array which contains all the accepted words ;remember user can give input in capital words also and we are converting it to lower using lower() function 
        while True:
            user_input = input(p_prompt)
            #'''if 0 > len(user_input) > 1:
                #print("Incorrect input: The input was not a single character, please try again.")'''
            if len(user_input) >= 1:  ### Check that input should be one character or more then one character
                if user_input.lower() in allowed_characters or user_input.lower() in allowed_strings:
                    return user_input
                else:
                    print("Incorrect input: The character was not in the allowed set of characters [" + allowed_characters + "], Please try again.")  
    # def input_number(p_Lower = 1, p_upper = 10, p_prompt = "")
    # if p_prompt == "":
    #     user_prompt = "Please enter a rating between " + str(p_lower) + " and " + str(p_upper) + ": "
    # else:
    #     user_prompt = p_prompt

    # while True:
    #     user_input = input(user_prompt)
    #     if user_input.isnumeric():
    #         if int(user_input) in range(p_lower, p_upper + 1):
    #             return int(user_input)
    #             else:
    #                 print("The number you entered is out of the range.\n")

def main_display_menu():
        print(" -------------------------- ---------- ------------------- ")
        print(" ******* Welcome to Contact Management Menu ******** ")
        print("Please choose one of the following options by inputting the first letter of the command or typing the whole word: ")
        print("     (L)ist - List All Contacts")
        print("     (A)dd - add a Contact to the list")
        print("     (E)dit - Edit a contact on the list")
        print("     (D)elete - Delete a contact on the list")
        print("     (Q)uit the program")

        print(" -------------------------- ---------- ------------------- ")

def main_loop():
    contacts = contact_list()
    while True:
            # display menu 
            # we have to use self before the function/method which is getting called 
            main_display_menu()
            # get a choice from user
            user_input = get_character("Please enter your choice: [a or d or e or l or q | Or type the word]: ")
            if user_input == 'a' or user_input == 'add':
                ### movie_list array is class variable; whose value is shared amonng all the instances of the class;
                ### this can be accessed using Movie_Management.movie_list from inside the class or outside the class also
                contacts.add_contact()    
            elif user_input == 'd' or user_input == 'delete':
                contacts.delete_contact()
            elif user_input == 'e' or user_input == 'edit':
                contacts.edit_contact()
            elif user_input == 'l' or user_input == 'list':
                contacts.print_contacts()
            elif user_input == 'q' or user_input == 'quit':
                print(" ********  Program Exit  ********")
                print("**** Bye ****")
                break
            user_continue = get_character("do you want to continue (y/n)?: ")
            if user_continue == "n":
                break

medi = main_loop()





    
