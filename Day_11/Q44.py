"""
PROBLEM STATEMENT:
Write a program to Write function to find factorial.
"""

def factorial(n):

    """The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. 
       To calculate the factorial, we can use a simple loop to multiply the numbers from 1 to n. 
       The time complexity of this approach is O(n), where n is the input number."""
    
    result = 1
    
    for i in range(1, n + 1):
    
        result *= i
        
    return result

number = int(input("Enter a non-negative integer: "))

if number < 0:
    
    print("Factorial is not defined for negative numbers.")

else:
    result = factorial(number)

    print(f"The factorial of {number} is: {result}")