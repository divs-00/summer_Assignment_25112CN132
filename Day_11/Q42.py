"""
PROBLEM STATEMENT:
Write a program to Write function to find maximum.
"""

def find_maximum(a, b):

    """Returns the maximum of two numbers a and b.
       This function compares the two numbers and returns the larger one. 
       The time complexity of this approach is O(1) since it performs a constant number of operations."""
    
    return a if a > b else b

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

result = find_maximum(num1, num2)

print(f"The maximum of {num1} and {num2} is: {result}")