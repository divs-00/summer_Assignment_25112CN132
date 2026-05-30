"""
PROBLEM STATEMENT:
Write a program to generate the Fibonacci sequence up to the Nth term.
"""

def fibonacci(n):

    """Returns a list containing the Fibonacci sequence up to the nth term.
       We can use an iterative approach to generate the sequence efficiently.
       The time complexity of this approach is O(n)."""
    
    sequence = []
    
    a, b = 0, 1
    
    for _ in range(n):
    
        sequence.append(a)
        
        a, b = b, a + b
        
    return sequence

num = int(input("Enter the number of terms in the Fibonacci sequence: "))

if num <= 0:

    print("Please enter a positive integer.")

else:

    result = fibonacci(num)

print(f"The Fibonacci sequence up to {num} terms is: {result}")