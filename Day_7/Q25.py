"""
PROBLEM STATEMENT:
Write a program to recursive factorial.
"""

def recursive_factorial(n):

    """The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. 
       To calculate the factorial recursively, 
       we can define the base case for n = 0 or n = 1, where the factorial is 1. 
       For n > 1, we can call the function recursively with n - 1 and multiply it by n. 
       The time complexity of this approach is O(n), where n is the input number."""
    
    if n == 0 or n == 1:
    
        return 1
        
    else:
    
        return n * recursive_factorial(n - 1)
    
number = int(input("Enter a non-negative integer: "))

if number < 0:
    
    print("Factorial is not defined for negative numbers.")

else:

    result = recursive_factorial(number)

    print(f"The factorial of {number} is: {result}")
