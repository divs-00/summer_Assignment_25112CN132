"""
PROBLEM STATEMENT:
Write a program to recursive fibonacci.
"""

def recursive_fibonacci(n):

    """The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
       To calculate the Fibonacci number recursively, we can define the base cases for n = 0 and n = 1, where the Fibonacci number is n itself. 
       For n > 1, we can call the function recursively with n - 1 and n - 2 and sum their results. 
       The time complexity of this approach is O(2^n), which can be inefficient for large values of n due to repeated calculations."""
    
    if n == 0:
    
        return 0
        
    elif n == 1:
    
        return 1
        
    else:
    
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
    
number = int(input("Enter a non-negative integer: "))

if number < 0:
    
    print("Fibonacci is not defined for negative numbers.")

else:

    result = recursive_fibonacci(number)

    print(f"The {number}th Fibonacci number is: {result}")