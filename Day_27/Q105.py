"""
PROBLEM STATEMENT:
Write a program to Create student record management system.
"""

def manage_student_records():

    """Manages student records by allowing creation, viewing, and searching.
       This function uses a list of dictionaries to store student details (ID, Name, and Grade).
       It provides an interactive menu for the user to perform CRUD-like operations dynamically.
       The time complexity for adding a record is O(1), and for searching it is O(n) in the worst case."""
    
    student_records = []
    
    while True:
        
        print("\n--- STUDENT RECORD MANAGEMENT SYSTEM ---")
        print("1. Add Student Record")
        print("2. View All Student Records")
        print("3. Search Student by ID")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grade = input("Enter Student Grade: ")
            
            student_dict = {
                "id": student_id,
                "name": name,
                "grade": grade
            }
            
            student_records.append(student_dict)
            print("Record added successfully!")
            
        elif choice == '2':
            
            if not student_records:
                
                print("No records found.")
                
            else:
                
                print("\n--- Student Records ---")
                
                for student in student_records:
                    
                    print(f"ID: {student['id']} | Name: {student['name']} | Grade: {student['grade']}")
                    
        elif choice == '3':
            
            search_id = input("Enter Student ID to search: ")
            found = False
            
            for student in student_records:
                
                if student['id'] == search_id:
                    
                    print(f"\nRecord Found! Name: {student['name']} | Grade: {student['grade']}")
                    found = True
                    break
                    
            if not found:
                
                print("Record not found.")
                
        elif choice == '4':
            
            print("Exiting the system. Goodbye!")
            break
            
        else:
            
            print("Invalid choice! Please select a valid option.")

manage_student_records()