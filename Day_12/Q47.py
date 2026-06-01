"""
PROBLEM STATEMENT:
Write a program to write function for fibonacci.
"""

def fibonacci(n):

    """Returns the nth Fibonacci number.
       The Fibonacci sequence is defined as follows:
       F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
       We will be using DMP (Dynamic Programming) approach to calculate the Fibonacci number efficiently.
       The time complexity of this approach is O(n) and the space complexity is also O(n) due to the memoization array."""
    
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    
    memo = [0] * (n + 1)

    memo[1] = 1
    
    for i in range(2, n + 1):
    
        memo[i] = memo[i - 1] + memo[i - 2]
    
    return memo[n]
    
n = int(input("Enter the position in the Fibonacci sequence: "))

try:

    result = fibonacci(n)

    print(f"The {n}th Fibonacci number is: {result}")

except ValueError as e:

    print(e)