"""
PROBLEM STATEMENT:
Write a program to Create menu-driven array operations system.
"""

class ArrayOperations:

    """Performs core operations on a dynamic sequential list (array).
       This class wraps a Python list to demonstrate array behaviors such as 
       insertion, deletion, searching, and traversal.
       The time complexities are: Traversal O(n), Search O(n), Insertion O(n), Deletion O(n)."""

    def __init__(self):
    
        self.array = []


    def traverse(self):
    
        """Iterates through the elements and prints the current status of the array.
           The time complexity is O(n), where n is the number of elements."""
           
        if not self.array:
        
            print("\nThe array is currently empty.")
            
            return
            
        print("\nCurrent Array Elements:")
        
        for idx, value in enumerate(self.array):
        
            print(f"Index {idx}: {value}")


    def insert_element(self, element, index=None):
    
        """Inserts an element into the array.
           If an index is provided, it places it at that position, shifting subsequent elements.
           Otherwise, it appends it to the end of the array."""
           
        if index is None:
        
            self.array.append(element)
            
            print(f"\nElement {element} appended to the end of the array.")
            
        else:
        
            if index < 0 or index > len(self.array):
            
                print(f"\nError: Index out of bounds. Valid range: 0 to {len(self.array)}.")
                
                return
                
            self.array.insert(index, element)
            
            print(f"\nElement {element} inserted successfully at index {index}.")


    def delete_element_by_index(self, index):
    
        """Removes an element from a specific position in the array.
           Shifts all subsequent elements to close the structural gap."""
           
        if index < 0 or index >= len(self.array):
        
            print(f"\nError: Index out of bounds. Valid range: 0 to {len(self.array) - 1}.")
            
            return
            
        removed_value = self.array.pop(index)
        
        print(f"\nSuccessfully removed element {removed_value} from index {index}.")


    def search_element(self, target):
    
        """Searches the array linearly to find the first occurrence of a target value.
           Returns the index if found, or notifies the user if it does not exist."""
           
        for idx, value in enumerate(self.array):
        
            if value == target:
            
                print(f"\nSuccess: Element {target} found at index {idx}.")
                
                return
                
        print(f"\nElement {target} was not found in the array.")


operations_system = ArrayOperations()

operations_system.insert_element(10)

operations_system.insert_element(20)

operations_system.insert_element(30)

while True:

    print("\n==============================")
    
    print("   ARRAY OPERATIONS SYSTEM")
    
    print("==============================")
    
    print("1. Display Array (Traverse)")
    
    print("2. Insert Element")
    
    print("3. Delete Element by Index")
    
    print("4. Search for Element")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        operations_system.traverse()
        
    elif choice == "2":
    
        try:
        
            element = int(input("Enter an integer element to insert: "))
            
            idx_input = input("Enter target index (Leave blank to append at end): ")
            
            if idx_input.strip() == "":
            
                operations_system.insert_element(element)
                
            else:
            
                operations_system.insert_element(element, int(idx_input))
                
        except ValueError:
        
            print("\nError: Please enter a valid integer choice.")
            
    elif choice == "3":
    
        if not operations_system.array:
        
            print("\nError: Cannot delete from an empty array.")
            
            continue
            
        try:
        
            index = int(input("Enter the index of the element to delete: "))
            
            operations_system.delete_element_by_index(index)
            
        except ValueError:
        
            print("\nError: Index must be a valid integer.")
            
    elif choice == "4":
    
        try:
        
            target = int(input("Enter the integer element to search for: "))
            
            operations_system.search_element(target)
            
        except ValueError:
        
            print("\nError: Target element must be an integer.")
            
    elif choice == "5":
    
        print("\nExiting the array system environment. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please provide a relative option number between 1 and 5.")