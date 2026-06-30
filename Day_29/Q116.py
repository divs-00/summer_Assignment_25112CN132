"""
PROBLEM STATEMENT:
Write a program to Create inventory management system.
"""

class InventoryManagement:

    """Performs core operations on an item repository (inventory).
       This class wraps a Python list of dictionaries to demonstrate data behaviors such as 
       tracking items, updating stock, searching products, and generating reports.
       The time complexities are: Traversal O(n), Search O(n), Insertion O(1), Deletion O(n)."""

    def __init__(self):
    
        self.inventory = []


    def display_inventory(self):
    
        """Iterates through the inventory list and prints the current status of all stock items.
           The time complexity is O(n), where n is the number of distinct items."""
           
        if not self.inventory:
        
            print("\nThe inventory is currently empty.")
            
            return
            
        print("\nCurrent Inventory Status:")
        
        for idx, item in enumerate(self.inventory):
        
            print(f"Index {idx} | ID: {item['id']} | Name: {item['name']} | Qty: {item['quantity']} | Price: ${item['price']:.2f}")


    def add_item(self, item_id, name, quantity, price):
    
        """Inserts a new item structure into the inventory array.
           Checks for existing item IDs first to prevent duplicate structural conflicts.
           Appends the new record directly to the end of the data list."""
           
        for item in self.inventory:
        
            if item['id'] == item_id:
            
                print(f"\nError: Item ID {item_id} already exists. Use update option instead.")
                
                return
                
        new_item = {
            'id': item_id,
            'name': name,
            'quantity': quantity,
            'price': price
        }
        
        self.inventory.append(new_item)
        
        print(f"\nItem '{name}' added successfully to the inventory record.")


    def remove_item_by_index(self, index):
    
        """Removes a stock item from a specific position in the inventory array.
           Shifts all subsequent entries to close the structural gap."""
           
        if index < 0 or index >= len(self.inventory):
        
            print(f"\nError: Index out of bounds. Valid range: 0 to {len(self.inventory) - 1}.")
            
            return
            
        removed_item = self.inventory.pop(index)
        
        print(f"\nSuccessfully removed '{removed_item['name']}' (ID: {removed_item['id']}) from index {index}.")


    def search_item(self, target_name):
    
        """Searches the inventory linearly to find items matching the target string name.
           Returns the matching information details or notifies if it does not exist."""
           
        found = False
        
        for idx, item in enumerate(self.inventory):
        
            if target_name.lower() in item['name'].lower():
            
                print(f"\nSuccess: Found match at index {idx} -> ID: {item['id']} | Name: {item['name']} | Stock: {item['quantity']}")
                
                found = True
                
        if not found:
        
            print(f"\nNo items matching '{target_name}' were found in the database.")


inventory_system = InventoryManagement()

inventory_system.add_item("101", "Wireless Mouse", 50, 24.99)

inventory_system.add_item("102", "Mechanical Keyboard", 35, 89.99)

inventory_system.add_item("103", "Gaming Monitor", 12, 299.50)

while True:

    print("\n==============================")
    
    print("  INVENTORY MANAGEMENT SYSTEM")
    
    print("==============================")
    
    print("1. Display Full Inventory")
    
    print("2. Add New Product Item")
    
    print("3. Remove Product by Index")
    
    print("4. Search Product by Name")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        inventory_system.display_inventory()
        
    elif choice == "2":
    
        try:
        
            item_id = input("Enter alpha-numeric item ID: ").strip()
            
            if not item_id:
            
                print("\nError: Item ID cannot be empty.")
                
                continue
                
            name = input("Enter product name: ").strip()
            
            quantity = int(input("Enter initial stock quantity: "))
            
            price = float(input("Enter product unit price: "))
            
            if quantity < 0 or price < 0:
            
                print("\nError: Quantity and Price parameters must be non-negative values.")
                
                continue
                
            inventory_system.add_item(item_id, name, quantity, price)
            
        except ValueError:
        
            print("\nError: Please enter a valid integer for quantity and decimal for price.")
            
    elif choice == "3":
    
        if not inventory_system.inventory:
        
            print("\nError: Cannot delete records from an empty inventory.")
            
            continue
            
        try:
        
            index = int(input("Enter the index of the item to delete: "))
            
            inventory_system.remove_item_by_index(index)
            
        except ValueError:
        
            print("\nError: Index must be a valid integer.")
            
    elif choice == "4":
    
        target_name = input("Enter product name search keyword: ").strip()
        
        if not target_name:
        
            print("\nError: Search string criteria cannot be empty.")
            
            continue
            
        inventory_system.search_item(target_name)
        
    elif choice == "5":
    
        print("\nExiting the inventory control console environment. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please provide a relative option number between 1 and 5.")