"""
PROBLEM STATEMENT:
Write a program to Create contact management system.
"""

class Contact:

    """Represents an individual contact profile.
       This class stores foundational personal details including a contact's
       name, phone number, email address, and a brief description/note."""

    def __init__(self, name, phone, email, notes=""):
    
        self.name = name
        
        self.phone = phone
        
        self.email = email
        
        self.notes = notes


class ContactSystem:

    """Manages an address book of individual contact records.
       It uses a dictionary mapping a contact's lowercased name to their profile 
       to prevent duplicates and ensure immediate retrieval.
       The time complexity to add, delete, or fetch a profile is O(1) on average."""

    def __init__(self):
    
        self.contacts = {}


    def add_contact(self, name, phone, email, notes=""):
    
        """Saves a new contact record into the address book directory.
           If the name already exists, it warns the user to avoid overwriting data."""
           
        key = name.strip().lower()
        
        if not key:
        
            print("\nError: Contact name cannot be blank.")
            
            return
            
        if key in self.contacts:
        
            print(f"\nError: A contact named '{name}' already exists.")
            
            return
            
        new_contact = Contact(name.strip(), phone.strip(), email.strip(), notes.strip())
        
        self.contacts[key] = new_contact
        
        print(f"\nContact '{name.strip()}' has been saved successfully!")


    def search_contact(self, name):
    
        """Finds and displays complete structural data for a requested contact profile.
           Performs a fast case-insensitive lookup check."""
           
        key = name.strip().lower()
        
        if key not in self.contacts:
        
            print(f"\nNo record found matching the name '{name}'.")
            
            return
            
        person = self.contacts[key]
        
        print("\n--- Contact Details ---")
        
        print(f"Name: {person.name}")
        
        print(f"Phone: {person.phone}")
        
        print(f"Email: {person.email}")
        
        print(f"Notes: {person.notes if person.notes else 'None'}")


    def delete_contact(self, name):
    
        """Removes an active contact from the directory using their profile name."""
        
        key = name.strip().lower()
        
        if key not in self.contacts:
        
            print(f"\nError: Could not delete. '{name}' does not exist.")
            
            return
            
        removed = self.contacts.pop(key)
        
        print(f"\nContact '{removed.name}' has been deleted from your address book.")


    def display_all_contacts(self):
    
        """Iterates through and prints every record stored inside the database."""
        
        if not self.contacts:
        
            print("\nYour contact directory is currently empty.")
            
            return
            
        print("\n--- Complete Address Book Directory ---")
        
        for idx, (key, person) in enumerate(self.contacts.items(), start=1):
        
            print(f"{idx}. {person.name} | Phone: {person.phone} | Email: {person.email}")


manager = ContactSystem()

manager.add_contact("John Doe", "555-0199", "john@example.com", "Work colleague")

manager.add_contact("Jane Watson", "555-0144", "jane@example.com", "College friend")

while True:

    print("\n==============================")
    
    print("   CONTACT MANAGEMENT SYSTEM")
    
    print("==============================")
    
    print("1. Display All Contacts")
    
    print("2. Add New Contact")
    
    print("3. Search Contact By Name")
    
    print("4. Delete a Contact")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        manager.display_all_contacts()
        
    elif choice == "2":
    
        name = input("Enter contact full name: ")
        
        phone = input("Enter phone number: ")
        
        email = input("Enter email address: ")
        
        notes = input("Enter any notes (optional): ")
        
        manager.add_contact(name, phone, email, notes)
        
    elif choice == "3":
    
        search_name = input("Enter the name of the contact to find: ")
        
        manager.search_contact(search_name)
        
    elif choice == "4":
    
        delete_name = input("Enter the name of the contact to remove: ")
        
        manager.delete_contact(delete_name)
        
    elif choice == "5":
    
        print("\nClosing your contact database. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please provide a relative option number between 1 and 5.")