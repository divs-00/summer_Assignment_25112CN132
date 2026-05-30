"""
PROBLEM STATEMENT:
Write a program to print prime numbers in a range.
"""

from Day_3.Q9 import is_prime

def check_prime_in_range(start, end):

    """Prints all prime numbers between start and end (inclusive).
       We can iterate through the numbers in the specified range and use the is_prime function to check for primality.
       The time complexity of this approach is O(n * sqrt(m)), 
       where n is the size of the range and m is the largest number in the range."""
    
    for num in range(start, end + 1):
    
        if is_prime(num):
        
            print(num, end=' ')

start_range = int(input("Enter the start of the range: "))

end_range = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start_range} and {end_range} are:")

check_prime_in_range(start_range, end_range)