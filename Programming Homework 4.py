#Programming Homework 4 Contact List
#Jeremiah Prokosch
#Contact list begins empty


#Class for contacts
class Contact:
    def __init__(self,p_id,p_fname,p_lname,p_age,p_phone,p_email):
        self.__id = p_id
        self.__fname = p_fname
        self.__lname = p_lname
        self.__age = p_age
        self.__phone = p_phone
        self.__email = p_email
    
    #Getters and setters
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(p_id):
        self.__id = p_id
    
    @property
    def fname(self):
        return self.__fname
    
    @fname.setter
    def fname(p_fname):
        self.__fname = p_fname

    @property
    def lname(self):
        return self.__lname
    
    @lname.setter
    def lname(p_lname):
        self.__lname = p_lname
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(p_age):
        self.__age = p_age
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(p_phone):
        self.__phone = p_phone
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(p_email):
        self.__email = p_email



#Class for Contact Lists
class Contact_list:
    def __init__(self):
        self.contact_list = []

    #Display the list of contacts.
    def list_contacts(self):
        print()
        if len(self.contact_list) == 0:
            print("Contact list is empty.")
        else:
            for entry in self.contact_list:
                print("ID: " + entry["ID"] + "\nName: " + entry["FName"] + "  " + entry["LName"] + "\nAge: " + entry["Age"] + "\nPhone: " + entry["Phone"] + "\nEmail: " + entry["Email"] + "\n")
        print()
        
    
    #Add a new contact to the contact list.
    def add_contact(self):     
        id = input("Enter the ID number between 1 and 1000 (inclusive) for the contact.\n")
        
        #Check for valid ID number.
        while (id.isalpha()) or (not float(id).is_integer()) or (int(id) > 1000 or int(id) < 1):
            print("Invalid entry. Try again.")
            id = input("Enter the ID number between 1 and 1000 (inclusive) for the contact.\n")
            
        fname = input("Enter the first name for the contact.\n")
        lname = input("Enter the last name for the contact.\n")
        age = input("Enter the age for the contact between 10 and 150 (inclusive).\n")
        
        #Check for valid age.
        while age.isalpha() or (not float(age).is_integer()) or (int(age) > 150 or int(age) < 10):
            print("Invalid entry. Try again.")
            age = input("Enter the age for the contact between 10 and 150 (inclusive).\n")

        #Checks for valid input for phone number.
        while True:
            phone = input("Enter the phone number for the contact.\n")
            loop = True
            checker = True
            while not len(phone) == 10:
                print("Non-phone number. Try again.")
                phone = input("Enter the phone number for the contact.\n")
            
            while loop:
                for iterator in range(0,len(phone)):
                    if phone[iterator].isalpha():
                        print("Non-phone number entry found. Try again.")
                        checker = False
                        loop = False
                    elif not phone[iterator].isalpha():
                        loop = False
                    loop = False
            if len(phone) == 10 and checker == True:
                break

        email = input("Enter the email for the contact.\n")
        print()

        contact_entry = Contact(id,fname,lname,age,phone,email)
        contact_dictionary = {"ID": contact_entry.id, "FName": contact_entry.fname, "LName": contact_entry.lname, "Age": contact_entry.age, "Phone": contact_entry.phone, "Email": contact_entry.email}
        self.contact_list.append(contact_dictionary)
        

    #Function for deleting contatcs.
    def delete_contact(self):
         print ("\nCurrent contact list")
         self.list_contacts()
         id_to_delete = input("Enter the ID of the contact you would like to delete.\n")

         for iterator in range(0, len(self.contact_list)):
             if self.contact_list[iterator]["ID"] == id_to_delete:
                 print("\n" + id_to_delete + " has been removed.\n")
                 self.contact_list.pop(iterator)
                 break
         return self.contact_list


    #Function for editing contacts in the list.
    def edit_contact(self):
        while True:
            user_choice = input("\nCOMMAND MENU \nWhat do you want to edit? \nEnter a integer between 1 and 6. \n1) First Name \n2) Last Name \n3) Age \n4) Phone Number \n5) Email \n6) Return with no changes\n")
            while user_choice.isalpha() or (not float(user_choice).is_integer()) or (int(user_choice) > 6 or int(user_choice) < 1):
                print("\nInvalid input. Try again.")
                user_choice = input("\nCOMMAND MENU \nWhat do you want to edit? \nEnter a integer between 1 and 6. \n1) First Name \n2) Last Name \n3) Age \n4) Phone Number \n5) Email \n6) Return with no changes\n")
            
            
            #Function for editing first name.
            if int(user_choice) == 1:
                print("Current Contact List")
                self.list_contacts()
                
                id_to_change = input("What is the ID of the contact you would like to update?\n")
                for iterator in range(0,len(self.contact_list)):
                    if self.contact_list[iterator]["ID"] == id_to_change:
                        new_fname = input("Enter the new first name.\n")
                        
                        while True:
                            print("Changing " + self.contact_list[iterator]["FName"] + " to " + new_fname)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.contact_list[iterator]["FName"] = new_fname
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            
            
            #Function for editing last name.            
            elif int(user_choice) == 2:
                print("Current Contact List")
                self.list_contacts()
                
                id_to_change = input("What is the ID of the contact you would like to update?\n")
                for iterator in range(0,len(self.contact_list)):
                    if self.contact_list[iterator]["ID"] == id_to_change:
                        new_lname = input("Enter the new last name.\n")
                        
                        while True:
                            print("Changing " + self.contact_list[iterator]["LName"] + " to " + new_lname)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.contact_list[iterator]["LName"] = new_lname
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            
            
            #Function for editing age.       
            elif int(user_choice) == 3:
                print("Current Contact List")
                self.list_contacts()
                
                id_to_change = input("What is the ID of the contact you would like to update?\n")
                for iterator in range(0,len(self.contact_list)):
                    if self.contact_list[iterator]["ID"] == id_to_change:
                        new_age = input("Enter the new age between 10 and 150 (inclusive).\n")
                        
                        #Check for valid age.
                        while new_age.isalpha() or (not float(new_age).is_integer()) or (int(new_age) > 150 or int(new_age) < 10):
                            print("Invalid age. Try again.")
                            new_age = input("Enter the new age between 10 and 150 (inclusive).\n")
                            
                        
                        while True:
                            print("Changing " + self.contact_list[iterator]["Age"] + " to " + new_age)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.contact_list[iterator]["Age"] = new_age
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            
            
            #Function for editing phone number.            
            elif int(user_choice) == 4:
                print("Current Contact List")
                self.list_contacts()
                
                id_to_change = input("What is the ID of the contact you would like to update?\n")
                for iterator in range(0,len(self.contact_list)):
                    if self.contact_list[iterator]["ID"] == id_to_change:
                        new_phone = ""
                        
                        #Checks for valid input for phone number.
                        while True:
                            new_phone = input("Enter the new phone number for the contact.\n")
                            loop = True
                            checker = True
                            while not len(new_phone) == 10:
                                print("Non-phone number. Try again.")
                                new_phone = input("Enter the new phone number for the contact.\n")
                            
                            while loop:
                                for item in range(0,len(new_phone)):
                                    if new_phone[item].isalpha():
                                        print("Non-phone number entry found. Try again.")
                                        checker = False
                                        loop = False
                                    elif not new_phone[item].isalpha():
                                        loop = False
                                    loop = False
                            if len(new_phone) == 10 and checker == True:
                                break
                        
                        while True:
                            print("Changing " + self.contact_list[iterator]["Phone"] + " to " + new_phone)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.contact_list[iterator]["Phone"] = new_phone
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            
            #Function for editing the email.
            elif int(user_choice) == 5:
                print("Current Contact List")
                self.list_contacts()
                
                id_to_change = input("What is the ID of the contact you would like to update?\n")
                for iterator in range(0,len(self.contact_list)):
                    if self.contact_list[iterator]["ID"] == id_to_change:
                        new_email = input("Enter the email.\n")
                        
                        while True:
                            print("Changing " + self.contact_list[iterator]["Email"] + " to " + new_email)
                            confirmation = input("Are you sure? (Yes or No)\n")
                            
                            if confirmation == "Y" or confirmation == "y" or confirmation == "Yes" or confirmation == "yes":
                                self.contact_list[iterator]["Email"] = new_email
                                break
                            elif confirmation == "N" or confirmation == "n" or confirmation == "No" or confirmation == "no":
                                break
                            else:
                                print("Not a valid selection. Try again.")
            
            #Function for returning the user the the prior menu.            
            elif int(user_choice) == 6:
                return self.contact_list

        return self.contact_list




# Function for running the base program and main menu.
def run_program():
    contacts = Contact_list()
    
    while True:
        user_input = input("\nCOMMAND MENU \nEnter a integer between 1 and 5. \n1) List Contacts \n2) Add Contacts \n3) Delete Contacts \n4) Edit Contacts \n5) Exit Program\n")
        # Loop checking for valid input.
        while user_input.isalpha() or (not float(user_input).is_integer()) or (int(user_input) < 1 or int(user_input) > 5):
            print("\nNot a valid selection. Try again.\n")
            user_input = input("\nCOMMAND MENU \nEnter a integer between 1 and 5. \n1) List Contacts \n2) Add Contacts \n3) Delete Contacts \n4) Edit Contacts \n5) Exit Program\n")
                 
        if 1 <= int(user_input) or int(user_input) <= 5:
            if int(user_input) == 1:
                contacts.list_contacts()
            elif int(user_input) == 2:
                contacts.add_contact()
            elif int(user_input) == 3:
                contacts.delete_contact()
            elif int(user_input) == 4:
                contacts.edit_contact()
            elif int(user_input) == 5:
                break


run_program()