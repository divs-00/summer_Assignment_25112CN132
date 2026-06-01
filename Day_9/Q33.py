"""
PROBLEM STATEMENT:
Write a program to Print reverse star pattern.
*****
****
***
**
*
"""

def reverse_star_pattern(n):

    """
    To print a reverse star pattern of height n, we can use a loop that iterates from n down to 1. 
    In each iteration, we print a number of stars equal to the current iteration number.
    The time complexity of this approach is O(n^2)."""
    
    for i in range(n, 0, -1):
    
        print('* ' * i)  # Print i stars followed by a space

        print()  # Move to the next line after each row

height = int(input("Enter the height of the reverse star pattern: "))

reverse_star_pattern(height)