"""
PROBLEM STATEMENT:
Write a program to Write function to find sum of two numbers.
"""

def sum_of_two_numbers(a, b):

    """Returns the sum of two numbers a and b.
       This is a straightforward function that takes two numbers as input and returns their sum.
       The time complexity of this approach is O(1) since it performs a constant number of operations."""
    
    return a + b

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

result = sum_of_two_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is: {result}")