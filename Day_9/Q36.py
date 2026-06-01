"""
PROBLEM STATEMENT:
Write a program to Print hollow square pattern.
*****
*   *
*   *
*   *
*****
"""

def hollow_square_pattern(n):

    """To print a hollow square pattern of size n, we can use nested loops. 
       The outer loop will iterate through each row, while the inner loop will iterate through each column. 
       We will print a star for the first and last row, and for the first and last column of each row. 
       For all other positions, we will print a space.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(n):

        for j in range(n):
        
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
        
                print('*', end='')  # Print star without moving to the next line
        
            else:
        
                print(' ', end='')  # Print space without moving to the next line
        
        print()  # Move to the next line after each row

size = int(input("Enter the size of the hollow square pattern: "))

hollow_square_pattern(size)