"""
PROBLEM STATEMENT:
Write a program to find factorial of a number.
"""

def factorial(n):

    """Returns the factorial of n using an iterative approach.
       The time complexity of this approach is O(n). 
       While the recursive approach also has a time complexity of O(n), 
       it can lead to stack overflow for large values of n. 
       The iterative approach is more efficient in terms of memory usage."""
    
    result = 1
    
    for i in range(2, n + 1):
    
        result *= i
    
    return result

num = int(input("Enter a number to find its factorial: "))

if num < 0:

    print("Factorial is not defined for negative numbers.")

else:

    result = factorial(num)

    print(f"The factorial of {num} is: {result}")