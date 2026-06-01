"""
PROBLEM STATEMENT:
Write a program to print half pyramid pattern.
"""

def half_pyramid_pattern(n):

    """To print a half pyramid pattern of height n, 
       we can use a loop that iterates from 1 to n. 
       In each iteration, we print a number of stars equal to the current iteration number."""
    
    for i in range(1, n + 1):
    
        print('* ' * i)  # Print i stars followed by a space

        print()  # Move to the next line after each row

height = int(input("Enter the height of the half pyramid: "))

half_pyramid_pattern(height)