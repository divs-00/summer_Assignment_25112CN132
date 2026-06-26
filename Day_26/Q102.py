"""
PROBLEM STATEMENT:
Write a program to Create voting eligibility system.
"""

def check_voting_eligibility(age):

    """Checks if a person is eligible to vote based on their age.
       This function validates that the age is a positive integer, then checks 
       if it meets the minimum voting requirement of 18 years.
       The time complexity of this evaluation is O(1)."""
    
    if age < 0:
    
        return "Invalid age entered. Age cannot be negative."
        
    if age >= 18:
    
        return "You are eligible to vote!"
        
    else:
    
        return f"You are not eligible to vote yet. Please wait {18 - age} more year(s)."

try:

    user_age = int(input("Enter your age: "))
    
    result = check_voting_eligibility(user_age)
    
    print(result)

except ValueError:

    print("Invalid input. Please enter a valid integer for age.")