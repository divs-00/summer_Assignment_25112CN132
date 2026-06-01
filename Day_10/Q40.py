"""
PROBLEM STATEMENT:
Write a program to Print character pyramid.
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""

def character_pyramid(n):

    """To print a character pyramid of height n, we can use nested loops. 
       The outer loop will iterate through each row, 
       while the inner loops will handle the spaces and characters. 
       For each row, we will print (n - i) spaces followed by characters 
       from 'A' to the current row's character and then back to 'A'.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(1, n + 1):
    
        # Print spaces
        print(' ' * (n - i), end='')

        # Print characters from 'A' to the current row's character
        for j in range(1, i + 1):
            
            print(chr(64 + j), end='')

        # Print characters from the current row's character back to 'A'
        for j in range(i - 1, 0, -1):

            print(chr(64 + j), end='')

        print()  # Move to the next line after each row

height = int(input("Enter the height of the character pyramid: "))

character_pyramid(height)