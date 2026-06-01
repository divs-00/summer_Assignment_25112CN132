"""
PROBLEM STATEMENT:
Write a program to Print star pyramid.
    *
   ***
  *****
 *******
*********
"""

def star_pyramid(n):

    """To print a star pyramid of height n, we can use nested loops. 
       The outer loop will iterate through each row, while the inner loop will handle the spaces and stars. 
       For each row, we will print (n - i) spaces followed by (2 * i - 1) stars, where i is the current row number.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(1, n + 1):
    
        # Print spaces
        print(' ' * (n - i), end='')

        # Print stars
        print('*' * (2 * i - 1))

height = int(input("Enter the height of the star pyramid: "))

star_pyramid(height)