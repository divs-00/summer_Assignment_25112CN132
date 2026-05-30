"""
PROBLEM STATEMENT:
Write a program to print Armsstrong numbers in a range.
"""

from Day_4.Q15  import is_armstrong

def is_armstrong_in_range(start, end):

    """Prints all Armstrong numbers between start and end (inclusive).
       We can iterate through the numbers in the specified range, 
       and use the is_armstrong function to check for Armstrong numbers.
       The time complexity of this approach is O(n * d), where n is the size of the range 
       and d is the number of digits in the largest number."""
    
    for num in range(start, end + 1):
    
        if is_armstrong(num):
        
            print(num, end=' ')

start_range = int(input("Enter the start of the range: "))

end_range = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start_range} and {end_range} are:")