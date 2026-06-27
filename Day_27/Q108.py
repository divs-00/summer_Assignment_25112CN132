"""
PROBLEM STATEMENT:
Write a program to Create marksheet generation system.
"""

def generate_marksheets():

    """Manages student marks and generates structured marksheets with performance metrics.
       This function tracks student subject scores, calculates total marks, percentage, and grade.
       It provides an interactive menu for entering scores, viewing all summaries, and generating full marksheets.
       The time complexity for adding marks is O(m), where m is the number of subjects, and for searching it is O(n)."""
    
    marksheet_records = []
    
    while True:
        
        print("\n--- MARKSHEET GENERATION SYSTEM ---")
        print("1. Add Student Marks")
        print("2. View All Student Summaries")
        print("3. Generate Full Marksheet by Roll Number")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            
            subjects = ["Mathematics", "Science", "English"]
            scores = {}
            total_marks = 0
            
            print("Enter marks obtained out of 100 for each subject:")
            
            for subject in subjects:
                
                score = float(input(f"Enter marks for {subject}: "))
                scores[subject] = score
                total_marks += score
                
            percentage = (total_marks / (len(subjects) * 100)) * 100
            
            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "Fail"
                
            student_data = {
                "roll_number": roll_number,
                "name": name,
                "scores": scores,
                "total": total_marks,
                "percentage": percentage,
                "grade": grade
            }
            
            marksheet_records.append(student_data)
            print("Marks recorded successfully!")
            
        elif choice == '2':
            
            if not marksheet_records:
                
                print("No records found.")
                
            else:
                
                print("\n--- Student Result Summaries ---")
                
                for student in marksheet_records:
                    
                    print(f"Roll No: {student['roll_number']} | Name: {student['name']} | Percentage: {student['percentage']:.2f}% | Grade: {student['grade']}")
                    
        elif choice == '3':
            
            search_roll = input("Enter Roll Number to generate marksheet: ")
            found = False
            
            for student in marksheet_records:
                
                if student['roll_number'] == search_roll:
                    
                    print("\n========================================")
                    print("               MARKSHEET                ")
                    print("========================================")
                    print(f"Roll Number : {student['roll_number']}")
                    print(f"Student Name: {student['name']}")
                    print("----------------------------------------")
                    print(f"{'Subject':<15} | {'Marks Obtained':<15} | {'Max Marks':<10}")
                    print("----------------------------------------")
                    
                    for subject, score in student['scores'].items():
                        
                        print(f"{subject:<15} | {score:<15.2f} | 100")
                        
                    print("----------------------------------------")
                    print(f"Total Marks : {student['total']:.2f} / 300")
                    print(f"Percentage  : {student['percentage']:.2f}%")
                    print(f"Final Grade : {student['grade']}")
                    print("========================================")
                    
                    found = True
                    break
                    
            if not found:
                
                print("Record not found for the given Roll Number.")
                
        elif choice == '4':
            
            print("Exiting the system. Goodbye!")
            break
            
        else:
            
            print("Invalid choice! Please select a valid option.")

generate_marksheets()