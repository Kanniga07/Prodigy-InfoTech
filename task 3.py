import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
                for contact in contacts_data:
                    self.contacts.append(Contact(**contact))

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts:
            print(contact)

    def edit_contact(self, old_name, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name == old_name:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                self.save_contacts()
                return
        print(f"Contact with name {old_name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_contacts()
                return
        print(f"Contact with name {name} not found.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            old_name = input("Enter the name of the contact to edit: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email address (leave blank to keep current): ")
            manager.edit_contact(old_name, new_name or None, new_phone or None, new_email or None)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
