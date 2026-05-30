"""
PROBLEM STATEMENT:
Write a program to find the nth Fibonacci number.
"""
from Day_4.Q13 import fibonacci

def fibonacci_term(n):

    """Returns the nth Fibonacci number.
       We can use the previously defined fibonacci function to get the sequence up to n terms 
       and return the last term. The time complexity of this approach is O(n)."""
    
    if n <= 0:
    
        return "Please enter a positive integer."
    
    else:
    
        sequence = fibonacci(n)
        
        return sequence[-1]

num = int(input("Enter the term number to find the Fibonacci number: "))

result = fibonacci_term(num)

print(f"The {num}th Fibonacci number is: {result}")