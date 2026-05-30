"""
PROBLEM STATEMENT:
Write a Python program to calculate the sum of the first N natural numbers.
"""

def natural_sum(n):

    """Returns the sum of the first n natural numbers.
       We can use the formula n(n + 1) / 2 to calculate the sum efficiently.
       The other options (iterative and recursive) would have a time complexity of O(n),
       while the formula has a time complexity of O(1)."""
    
    return n * (n + 1) // 2

num = int(input("Enter a natural number: "))

result = natural_sum(num)

print(f"The sum of the first {num} natural numbers is: {result}")