"""
PROBLEM STATEMENT:
Write a program to Create salary management system.
"""

def manage_salary_records():

    """Manages employee salary records by allowing creation, viewing, and searching.
       This function uses a list of dictionaries to store financial details (ID, Name, and Net Salary).
       It provides an interactive menu for calculating allowances, deductions, and tracking payroll.
       The time complexity for adding a record is O(1), and for searching it is O(n) in the worst case."""
    
    salary_records = []
    
    while True:
        
        print("\n--- SALARY MANAGEMENT SYSTEM ---")
        print("1. Add Salary Record")
        print("2. View All Salary Records")
        print("3. Search Salary Record by Employee ID")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            base_salary = float(input("Enter Base Salary: "))
            allowances = float(input("Enter Allowances: "))
            deductions = float(input("Enter Deductions: "))
            
            net_salary = base_salary + allowances - deductions
            
            salary_dict = {
                "id": employee_id,
                "name": name,
                "base_salary": base_salary,
                "allowances": allowances,
                "deductions": deductions,
                "net_salary": net_salary
            }
            
            salary_records.append(salary_dict)
            print("Salary record added successfully!")
            
        elif choice == '2':
            
            if not salary_records:
                
                print("No records found.")
                
            else:
                
                print("\n--- Salary Records ---")
                
                for record in salary_records:
                    
                    print(f"ID: {record['id']} | Name: {record['name']} | Net Salary: {record['net_salary']:.2f}")
                    
        elif choice == '3':
            
            search_id = input("Enter Employee ID to search: ")
            found = False
            
            for record in salary_records:
                
                if record['id'] == search_id:
                    
                    print(f"\nRecord Found!")
                    print(f"Name: {record['name']}")
                    print(f"Base Salary: {record['base_salary']:.2f}")
                    print(f"Allowances: {record['allowances']:.2f}")
                    print(f"Deductions: {record['deductions']:.2f}")
                    print(f"Net Payable Salary: {record['net_salary']:.2f}")
                    found = True
                    break
                    
            if not found:
                
                print("Record not found.")
                
        elif choice == '4':
            
            print("Exiting the system. Goodbye!")
            break
            
        else:
            
            print("Invalid choice! Please select a valid option.")

manage_salary_records()