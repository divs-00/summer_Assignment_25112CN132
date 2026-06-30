"""
PROBLEM STATEMENT:
Write a program to Develop complete mini project using arrays, strings and functions.
"""

class MiniProject:

    """Performs core operations of a mini project using arrays, strings, and functions.
       This class uses a Python list (array) and string processing techniques to demonstrate
       insertion, deletion, searching, traversal, and string manipulation operations.
       The time complexities are: Traversal O(n), Search O(n), Insertion O(n), Deletion O(n)."""

    def __init__(self):
    
        self.data = []


    def traverse(self):
    
        """Displays all elements stored in the array.
           The time complexity is O(n), where n is the number of elements."""
           
        if not self.data:
        
            print("\nThe data structure is currently empty.")
            
            return
            
        print("\nCurrent Elements:")
        
        for index, value in enumerate(self.data):
        
            print(f"Index {index}: {value}")


    def insert_element(self, element):
    
        """Inserts a new string element into the array."""
        
        self.data.append(element)
        
        print(f"\nElement '{element}' inserted successfully.")


    def delete_element(self, element):
    
        """Deletes an element from the array if it exists."""
        
        if element in self.data:
        
            self.data.remove(element)
            
            print(f"\nElement '{element}' deleted successfully.")
            
        else:
        
            print(f"\nError: Element '{element}' not found.")


    def search_element(self, element):
    
        """Searches for an element in the array."""
        
        for index, value in enumerate(self.data):
        
            if value == element:
            
                print(f"\nElement '{element}' found at index {index}.")
                
                return
                
        print(f"\nElement '{element}' not found.")


    def update_element(self, old, new):
    
        """Updates an existing string element with a new string value."""
        
        for index in range(len(self.data)):
        
            if self.data[index] == old:
            
                self.data[index] = new
                
                print(f"\nElement '{old}' updated to '{new}'.")
                
                return
                
        print(f"\nError: Element '{old}' not found.")


    def string_operations(self, text):
    
        """Performs basic string operations like length, uppercase, lowercase, and reversal."""
        
        print("\nSTRING OPERATIONS")
        
        print(f"Original String: {text}")
        
        print(f"Length: {len(text)}")
        
        print(f"Uppercase: {text.upper()}")
        
        print(f"Lowercase: {text.lower()}")
        
        print(f"Reversed: {text[::-1]}")


project = MiniProject()

project.insert_element("apple")

project.insert_element("banana")

project.insert_element("cherry")

while True:

    print("\n==============================")
    
    print("      MINI PROJECT SYSTEM")
    
    print("==============================")
    
    print("1. Display Elements")
    
    print("2. Insert Element")
    
    print("3. Delete Element")
    
    print("4. Search Element")
    
    print("5. Update Element")
    
    print("6. String Operations")
    
    print("7. Exit")
    
    choice = input("\nEnter your choice (1-7): ")
    
    if choice == "1":
    
        project.traverse()
        
    elif choice == "2":
    
        element = input("Enter string element to insert: ")
        
        project.insert_element(element)
        
    elif choice == "3":
    
        element = input("Enter element to delete: ")
        
        project.delete_element(element)
        
    elif choice == "4":
    
        element = input("Enter element to search: ")
        
        project.search_element(element)
        
    elif choice == "5":
    
        old = input("Enter element to replace: ")
        
        new = input("Enter new element: ")
        
        project.update_element(old, new)
        
    elif choice == "6":
    
        text = input("Enter a string for operations: ")
        
        project.string_operations(text)
        
    elif choice == "7":
    
        print("\nExiting Mini Project System.")
        
        break
        
    else:
    
        print("\nInvalid choice. Please select a valid option (1-7).")