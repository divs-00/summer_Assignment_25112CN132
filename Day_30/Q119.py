"""
PROBLEM STATEMENT:
Write a program to Create mini employee management system.
"""

class EmployeeManagement:

    """Performs core operations on a mini employee management system.
       This class wraps a Python dictionary to demonstrate employee record behaviors such as
       insertion, deletion, searching, updating, and traversal of employee data.
       The time complexities are: Traversal O(n), Search O(1), Insertion O(1), Deletion O(1), Update O(1)."""

    def __init__(self):
    
        self.employees = {}


    def traverse(self):
    
        """Iterates through the employee database and displays all employee records.
           The time complexity is O(n), where n is the number of employees."""
           
        if not self.employees:
        
            print("\nThe employee database is currently empty.")
            
            return
            
        print("\nCurrent Employee Records:")
        
        for emp_id, value in self.employees.items():
        
            print(f"Employee ID: {emp_id}")
            
            print(f"Name: {value['name']}")
            
            print(f"Department: {value['department']}")


    def insert_employee(self, emp_id, name, department):
    
        """Inserts a new employee record into the database."""
        
        if emp_id in self.employees:
        
            print("\nError: Employee ID already exists.")
            
            return
            
        self.employees[emp_id] = {
        
            "name": name,
            
            "department": department
            
        }
        
        print(f"\nEmployee {name} inserted successfully.")


    def delete_employee(self, emp_id):
    
        """Deletes an employee record from the database using employee ID."""
        
        if emp_id not in self.employees:
        
            print("\nError: Employee ID not found.")
            
            return
            
        removed_value = self.employees.pop(emp_id)
        
        print(f"\nSuccessfully removed employee {removed_value['name']}.")


    def search_employee(self, emp_id):
    
        """Searches for an employee in the database using employee ID."""
        
        if emp_id in self.employees:
        
            value = self.employees[emp_id]
            
            print(f"\nEmployee Found:")
            
            print(f"Employee ID: {emp_id}")
            
            print(f"Name: {value['name']}")
            
            print(f"Department: {value['department']}")
            
            return
            
        print("\nEmployee not found.")


employee_system = EmployeeManagement()

employee_system.insert_employee(101, "Rahul", "HR")

employee_system.insert_employee(102, "Priya", "Finance")

employee_system.insert_employee(103, "Amit", "IT")

while True:

    print("\n==============================")
    
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    
    print("==============================")
    
    print("1. Display Employees")
    
    print("2. Insert Employee")
    
    print("3. Delete Employee")
    
    print("4. Search Employee")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        employee_system.traverse()
        
    elif choice == "2":
    
        try:
        
            emp_id = int(input("Enter Employee ID: "))
            
            name = input("Enter Employee Name: ")
            
            department = input("Enter Department: ")
            
            employee_system.insert_employee(emp_id, name, department)
            
        except ValueError:
        
            print("\nError: Invalid input. Employee ID must be an integer.")
            
    elif choice == "3":
    
        try:
        
            emp_id = int(input("Enter Employee ID to delete: "))
            
            employee_system.delete_employee(emp_id)
            
        except ValueError:
        
            print("\nError: Invalid input. Employee ID must be an integer.")
            
    elif choice == "4":
    
        try:
        
            emp_id = int(input("Enter Employee ID to search: "))
            
            employee_system.search_employee(emp_id)
            
        except ValueError:
        
            print("\nError: Invalid input. Employee ID must be an integer.")
            
    elif choice == "5":
    
        print("\nExiting Employee Management System.")
        
        break
        
    else:
    
        print("\nInvalid choice. Please select a valid option (1-5).")