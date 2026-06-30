"""
PROBLEM STATEMENT:
Write a program to Create mini library system.
"""

class MiniLibrary:

    """Performs core operations on a library books database.
       This class wraps a Python dictionary to demonstrate catalog behaviors such as 
       adding, borrowing, returning, searching, and displaying books.
       The time complexities are: Display O(n), Search O(1), Insertion/Update O(1), Modification O(1)."""

    def __init__(self):
    
        self.library = {}


    def display_books(self):
    
        """Iterates through the library catalog and prints the current status of all books.
           The time complexity is O(n), where n is the total number of books."""
           
        if not self.library:
        
            print("\nThe library is currently empty.")
            
            return
            
        print("\nCurrent Library Catalog:")
        
        for book_id, details in self.library.items():
        
            status = "Available" if details['is_available'] else "Borrowed"
            
            print(f"ID: {book_id} | Title: {details['title']} | Author: {details['author']} | Status: {status}")


    def add_book(self, book_id, title, author):
    
        """Adds a brand new book to the library system.
           If the specified Book ID already exists, it prompts an error to maintain unique copies."""
           
        if book_id in self.library:
        
            print(f"\nError: Book ID {book_id} already exists with title '{self.library[book_id]['title']}'.")
            
        else:
        
            self.library[book_id] = {"title": title, "author": author, "is_available": True}
            
            print(f"\nNew Book '{title}' by {author} added successfully to the library catalog.")


    def borrow_book(self, book_id):
    
        """Checks out a book using its unique Book ID.
           Updates its availability status to False if it is available for borrowing."""
           
        if book_id not in self.library:
        
            print(f"\nError: Book ID {book_id} does not exist in the library catalog.")
            
            return
            
        if not self.library[book_id]["is_available"]:
        
            print(f"\nError: '{self.library[book_id]['title']}' is currently borrowed by someone else.")
            
            return
            
        self.library[book_id]["is_available"] = False
        
        print(f"\nSuccessfully borrowed '{self.library[book_id]['title']}'. Enjoy your reading!")


    def return_book(self, book_id):
    
        """Returns a borrowed book back to the library using its Book ID.
           Reverts its availability status back to True."""
           
        if book_id not in self.library:
        
            print(f"\nError: Book ID {book_id} does not belong to this library system.")
            
            return
            
        if self.library[book_id]["is_available"]:
        
            print(f"\nError: '{self.library[book_id]['title']}' was already returned and is already available.")
            
            return
            
        self.library[book_id]["is_available"] = True
        
        print(f"\nSuccessfully returned '{self.library[book_id]['title']}'. Thank you!")


    def search_book(self, book_id):
    
        """Searches the library mapping directly to find book records by ID.
           Returns and prints specific status records instantly if it exists."""
           
        if book_id in self.library:
        
            details = self.library[book_id]
            
            status = "Available" if details['is_available'] else "Borrowed"
            
            print(f"\nSuccess: Book ID {book_id} found.")
            
            print(f"-> Title: {details['title']}\n-> Author: {details['author']}\n-> Current Status: {status}")
            
            return
            
        print(f"\nBook ID {book_id} was not found in the library catalog.")


library_system = MiniLibrary()

library_system.add_book("B101", "To Kill a Mockingbird", "Harper Lee")

library_system.add_book("B102", "1984", "George Orwell")

library_system.add_book("B103", "The Great Gatsby", "F. Scott Fitzgerald")

while True:

    print("\n==============================")
    
    print("      MINI LIBRARY SYSTEM")
    
    print("==============================")
    
    print("1. Display Entire Catalog")
    
    print("2. Add New Book")
    
    print("3. Borrow a Book")
    
    print("4. Return a Book")
    
    print("5. Search for Book by ID")
    
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == "1":
    
        library_system.display_books()
        
    elif choice == "2":
    
        book_id = input("Enter unique Book ID: ").strip()
        
        if not book_id:
        
            print("\nError: Book ID cannot be blank.")
            
            continue
            
        title = input("Enter Book Title: ").strip()
        
        if not title:
        
            print("\nError: Book Title cannot be blank.")
            
            continue
            
        author = input("Enter Author Name: ").strip()
        
        if not author:
        
            print("\nError: Author Name cannot be blank.")
            
            continue
            
        library_system.add_book(book_id, title, author)
            
    elif choice == "3":
    
        if not library_system.library:
        
            print("\nError: Cannot borrow from an empty library catalog.")
            
            continue
            
        book_id = input("Enter the Book ID to borrow: ").strip()
        
        library_system.borrow_book(book_id)
        
    elif choice == "4":
    
        if not library_system.library:
        
            print("\nError: Cannot return books to an empty library catalog.")
            
            continue
            
        book_id = input("Enter the Book ID to return: ").strip()
        
        library_system.return_book(book_id)
        
    elif choice == "5":
    
        book_id = input("Enter the Book ID to search for: ").strip()
        
        library_system.search_book(book_id)
        
    elif choice == "6":
    
        print("\nExiting the library system environment. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please provide a relative option number between 1 and 6.")