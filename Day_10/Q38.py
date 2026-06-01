"""
PROBLEM STATEMENT:
Write a program to Print reverse pyramid.
*********
 *******
  *****
   ***
    *
"""

def reverse_pyramid(n):

    """To print a reverse pyramid of height n, we can use nested loops. 
       The outer loop will iterate through each row, while the inner loop will handle the spaces and stars. 
       For each row, we will print (i - 1) spaces followed by (2 * (n - i) + 1) stars, where i is the current row number.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(1, n + 1):
    
        # Print spaces
        print(' ' * (i - 1), end='')

        # Print stars
        print('*' * (2 * (n - i) + 1))

height = int(input("Enter the height of the reverse pyramid: "))

reverse_pyramid(height)