"""
PROBLEM STATEMENT:
Write a program to Print number pyramid.
    1
   121
  12321
 1234321
123454321
"""

def number_pyramid(n):

    """To print a number pyramid of height n, we can use nested loops. 
       The outer loop will iterate through each row, while the inner loop will handle the spaces and numbers. 
       For each row, we will print (n - i) spaces followed by the numbers from 1 to i 
       and then from (i - 1) back to 1, where i is the current row number.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(1, n + 1):
    
        # Print spaces
        print(' ' * (n - i), end='')

        # Print increasing numbers
        for j in range(1, i + 1):

            print(j, end='')

        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            
            print(j, end='')

        print()  # Move to the next line after each row

height = int(input("Enter the height of the number pyramid: "))

number_pyramid(height)