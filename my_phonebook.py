class Contact:
    def __init__(self, number, name, email):
        self.number = number
        self.name = name
        self.email = email
class PhoneBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, number, email):
        if name in self.contacts:
            print("This contact already exists")
        else:
            if number.startswith("+") and "@" in email:
                self.contacts[name] = Contact(number, name, email)
                print(f'Contact {name} has been  added successfully!')
            elif not number.startswith("+"):
                print("Number must start with +")
            elif "@" not in email:
                print("Email must be with @")
            else:
                print("Undefined error, try again")
    def view_contacts(self):
        if self.contacts:
            print("Your contact list:")
            for contact in self.contacts.values():
                print(f'Name: {contact.name}\nNumber: {contact.number}\nEmail: {contact.email}')
        else:
            print("No contacts")
    def search_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Contact found with name:{contact.name}\n Number: {contact.number}\nEmail: {contact.email}")
        else:
            print("Contact does not exist")
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} has been deleted')
        else: print("Contact does not exist")
    def edit_contact(self, name, new_number, new_email):
        if name in self.contacts:
            contact = self.contacts[name]
            contact.number = new_number
            contact.email = new_email
            print(f'Contact {name} has been successfully updated!')
        else:
            print("Contact does not exist")

phone_book = PhoneBook()
while True:
    choice = input("Welcome to the PhoneBook! Please enter what you would like to do:\n1-Add a contact\n2-View all contacts\n3-search a contact\n4-delete a contact\n5-edit a contact\n6-exit\n")
    if choice == '1':
        name = input("Enter a name: ")
        number = input("Enter a number(must start with '+': ")
        email = input("Enter an email:")
        phone_book.add_contact(name, number, email)
    elif choice == '2':
        phone_book.view_contacts()
    elif choice == "3":
        name = input("Enter a name you want to find: ")
        phone_book.search_contact(name)
    elif choice == "4":
        name = input("Enter a contact you want to delete: ")
        phone_book.delete_contact(name)
    elif choice == "5":
        name = input("Enter a contact you want to edit: ")
        new_number = input("Enter a new phone number(starts with +)")
        new_email = input("Enter a new email(must have @)")
        phone_book.edit_contact(name, new_number,new_email)
    elif choice == "6":
        break
    else:
        print("Invalid")



