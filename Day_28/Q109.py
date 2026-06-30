"""
PROBLEM STATEMENT:
Write a program to Create library management system.
"""

class Book:

    """Represents a book in the library system.
       This class stores details about a book including its ISBN, title, author,
       and its current availability status."""

    def __init__(self, isbn, title, author):
    
        self.isbn = isbn
        
        self.title = title
        
        self.author = author
        
        self.is_available = True


class Library:

    """Manages a collection of books and checkout transactions.
       This class allows adding new books, checking out books to users, and returning books.
       It uses a dictionary for book storage to ensure fast lookups by ISBN.
       The time complexity for adding, checking out, and returning a book is O(1) on average."""

    def __init__(self):
    
        self.books = {}


    def add_book(self, isbn, title, author):
    
        """Adds a new book to the library system.
           If the book already exists, it prompts the user accordingly."""
           
        if isbn in self.books:
        
            print(f"\nBook with ISBN {isbn} already exists in the system.")
            
            return
            
        new_book = Book(isbn, title, author)
        
        self.books[isbn] = new_book
        
        print(f"\nBook '{title}' added successfully!")


    def checkout_book(self, isbn):
    
        """Checks out a book from the library using its ISBN.
           Changes the availability status of the book to False if it is available."""
           
        if isbn not in self.books:
        
            print("\nError: Book not found in the library system.")
            
            return
            
        book = self.books[isbn]
        
        if not book.is_available:
        
            print(f"\nSorry, '{book.title}' is currently checked out.")
            
            return
            
        book.is_available = False
        
        print(f"\nYou have successfully checked out '{book.title}'.")


    def return_book(self, isbn):
    
        """Returns a borrowed book back to the library using its ISBN.
           Restores the availability status of the book to True."""
           
        if isbn not in self.books:
        
            print("\nError: Book not found in the library system.")
            
            return
            
        book = self.books[isbn]
        
        if book.is_available:
        
            print(f"\nError: '{book.title}' was not checked out.")
            
            return
            
        book.is_available = True
        
        print(f"\nThank you! '{book.title}' has been returned successfully.")


    def display_books(self):
    
        """Displays all the books currently registered in the library system
           along with their current availability status."""
           
        if not self.books:
        
            print("\nThe library is currently empty.")
            
            return
            
        print("\n--- Library Catalog ---")
        
        for isbn, book in self.books.items():
        
            status = "Available" if book.is_available else "Checked Out"
            
            print(f"ISBN: {isbn} | Title: {book.title} | Author: {book.author} | Status: {status}")


library = Library()

library.add_book("111", "The Hobbit", "J.R.R. Tolkien")

library.add_book("222", "1984", "George Orwell")

while True:

    print("\n==============================")
    
    print("  LIBRARY MANAGEMENT SYSTEM")
    
    print("==============================")
    
    print("1. Display All Books")
    
    print("2. Add a New Book")
    
    print("3. Check Out a Book")
    
    print("4. Return a Book")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        library.display_books()
        
    elif choice == "2":
    
        isbn = input("Enter ISBN: ")
        
        title = input("Enter Title: ")
        
        author = input("Enter Author: ")
        
        library.add_book(isbn, title, author)
        
    elif choice == "3":
    
        isbn = input("Enter ISBN of the book to check out: ")
        
        library.checkout_book(isbn)
        
    elif choice == "4":
    
        isbn = input("Enter ISBN of the book to return: ")
        
        library.return_book(isbn)
        
    elif choice == "5":
    
        print("\nExiting the library system. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please enter a number between 1 and 5.")