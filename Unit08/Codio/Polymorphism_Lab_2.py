"""
Initialization: Changed self.view from 'quit' to 'list' in the __init__ method to show the list view first.
show_list Method: Modified to check if self.contact_list is empty. If empty, it prompts the user to add a contact or quit. If not, it sets the view to 'quit'.
handle_choice Method: Evaluates the user's choice to either add a new contact or quit.
Information Class: Defined to store contact details.
add_contact Method: Overloaded the + operator to add an Information object to self.contact_list and set the view back to 'list'.
Testing: Added test code at the end to create a Contacts object, display the menu, and check that a contact is added to the list.
"""

class Contacts:
    def __init__(self):
        self.view = 'list'
        self.contact_list = []
        self.choice = None
        self.index = None

    def display(self):
        while True:
            if self.view == 'list':
                self.show_list()
            elif self.view == 'info':
                self.show_info()
            elif self.view == 'add':
                print()
                self.add_contact()
            elif self.view == 'quit':
                print('\nClosing the contact list...\n')
                break

    def show_list(self):
        print()
        if len(self.contact_list) == 0:
            self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            self.view = 'quit'
        self.handle_choice()

    def show_info(self):
        pass

    def add_contact(self):
        self + Information()
        self.view = 'list'

    def handle_choice(self):
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'

    def __add__(self, new_contact):
        self.contact_list.append(new_contact)

class Information:
    def __init__(self):
        self.first_name = input('Enter their first name: ')
        self.last_name = input('Enter their last name: ')
        self.personal_phone = input('Enter their personal phone number: ')
        self.personal_email = input('Enter their personal email address: ')
        self.work_phone = input('Enter their work phone number: ')
        self.work_email = input('Enter their work email address: ')
        self.title = input('Enter their work title: ')

# Testing the code
contacts = Contacts()
contacts.display()
print(len(contacts.contact_list))
