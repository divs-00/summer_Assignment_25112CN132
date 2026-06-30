"""
PROBLEM STATEMENT:
Write a program to Create student record system using arrays and strings.
"""

class StudentRecordSystem:

    """Performs core operations on a collection of student data records.
       This class manages parallel information fields using strings and data blocks to
       demonstrate array-like structures for tracking names, IDs, and grade criteria.
       The time complexities are: Traversal O(n), Search O(n), Insertion O(1), Deletion O(n)."""

    def __init__(self):
    
        self.records = []


    def display_records(self):
    
        """Iterates through the record entries and prints the current status of all students.
           The time complexity is O(n), where n is the number of student profiles."""
           
        if not self.records:
        
            print("\nThe student record system is currently empty.")
            
            return
            
        print("\nCurrent Student Records:")
        
        for idx, student in enumerate(self.records):
        
            print(f"Index {idx} | Roll No: {student['roll_no']} | Name: {student['name']} | Major: {student['major']} | GPA: {student['gpa']:.2f}")


    def add_student(self, roll_no, name, major, gpa):
    
        """Inserts a new student profile into the sequential structural array.
           Validates that unique string identifier attributes do not conflict.
           Appends the formatted record mapping to the database array."""
           
        for student in self.records:
        
            if student['roll_no'].lower() == roll_no.lower():
            
                print(f"\nError: Student Roll Number '{roll_no}' already exists in system tracks.")
                
                return
                
        new_student = {
            'roll_no': roll_no,
            'name': name,
            'major': major,
            'gpa': gpa
        }
        
        self.records.append(new_student)
        
        print(f"\nRecord for student '{name}' successfully committed to storage tracks.")


    def delete_record_by_index(self, index):
    
        """Removes a student tracking block from a specific position in the array structure.
           Shifts all subsequent entry indices to maintain unified data contiguity."""
           
        if index < 0 or index >= len(self.records):
        
            print(f"\nError: Index out of bounds. Valid range: 0 to {len(self.records) - 1}.")
            
            return
            
        removed_profile = self.records.pop(index)
        
        print(f"\nSuccessfully purged '{removed_profile['name']}' (Roll No: {removed_profile['roll_no']}) from index {index}.")


    def search_student_by_name(self, target_name):
    
        """Searches the string entries linearly to locate matching student names.
           Prints all instances where the target string segment matches records."""
           
        found = False
        
        for idx, student in enumerate(self.records):
        
            if target_name.lower() in student['name'].lower():
            
                print(f"\nSuccess: Record match at index {idx} -> Roll No: {student['roll_no']} | Name: {student['name']} | GPA: {student['gpa']}")
                
                found = True
                
        if not found:
        
            print(f"\nNo student records containing string sequence '{target_name}' were located.")


student_system = StudentRecordSystem()

student_system.add_student("S101", "Alice Vance", "Computer Science", 3.85)

student_system.add_student("S102", "Bob Miller", "Data Analytics", 3.42)

student_system.add_student("S103", "Charlie Cross", "Electrical Engineering", 3.91)

while True:

    print("\n==============================")
    
    print("    STUDENT RECORD SYSTEM")
    
    print("==============================")
    
    print("1. Display All Student Records")
    
    print("2. Insert New Student Record")
    
    print("3. Delete Record by Index")
    
    print("4. Search Student by Name String")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        student_system.display_records()
        
    elif choice == "2":
    
        try:
        
            roll_no = input("Enter alpha-numeric roll number string: ").strip()
            
            if not roll_no:
            
                print("\nError: Roll number attribute cannot remain blank.")
                
                continue
                
            name = input("Enter full student name string: ").strip()
            
            major = input("Enter academic major program description: ").strip()
            
            gpa = float(input("Enter floating-point numeric GPA (0.00 - 4.00): "))
            
            if gpa < 0.0 or gpa > 4.0:
            
                print("\nError: GPA evaluation metric out of valid range constraints.")
                
                continue
                
            student_system.add_student(roll_no, name, major, gpa)
            
        except ValueError:
        
            print("\nError: Invalid character evaluation detected for numeric grade scales.")
            
    elif choice == "3":
    
        if not student_system.records:
        
            print("\nError: Execution halted. Current data list is unpopulated.")
            
            continue
            
        try:
        
            index = int(input("Enter the structural array index to purge: "))
            
            student_system.delete_record_by_index(index)
            
        except ValueError:
        
            print("\nError: Array offset parameter must be a valid system integer.")
            
    elif choice == "4":
    
        target_name = input("Enter partial or whole student identity name string: ").strip()
        
        if not target_name:
        
            print("\nError: Target character match string criteria cannot be blank.")
            
            continue
            
        student_system.search_student_by_name(target_name)
        
    elif choice == "5":
    
        print("\nExiting the academic tracking environment. System log off complete!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please provide a relative option number between 1 and 5.")