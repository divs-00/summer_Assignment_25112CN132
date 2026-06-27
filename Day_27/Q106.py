"""
PROBLEM STATEMENT:
Write a program to Create employee management system.
"""

def manage_employee_records():

    """Manages employee records by allowing creation, viewing, and searching.
       This function uses a list of dictionaries to store employee details (ID, Name, and Department).
       It provides an interactive menu for the user to perform CRUD-like operations dynamically.
       The time complexity for adding a record is O(1), and for searching it is O(n) in the worst case."""
    
    employee_records = []
    
    while True:
        
        print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
        print("1. Add Employee Record")
        print("2. View All Employee Records")
        print("3. Search Employee by ID")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            
            employee_dict = {
                "id": employee_id,
                "name": name,
                "department": department
            }
            
            employee_records.append(employee_dict)
            print("Record added successfully!")
            
        elif choice == '2':
            
            if not employee_records:
                
                print("No records found.")
                
            else:
                
                print("\n--- Employee Records ---")
                
                for employee in employee_records:
                    
                    print(f"ID: {employee['id']} | Name: {employee['name']} | Department: {employee['department']}")
                    
        elif choice == '3':
            
            search_id = input("Enter Employee ID to search: ")
            found = False
            
            for employee in employee_records:
                
                if employee['id'] == search_id:
                    
                    print(f"\nRecord Found! Name: {employee['name']} | Department: {employee['department']}")
                    found = True
                    break
                    
            if not found:
                
                print("Record not found.")
                
        elif choice == '4':
            
            print("Exiting the system. Goodbye!")
            break
            
        else:
            
            print("Invalid choice! Please select a valid option.")

manage_employee_records()