"""
PROBLEM STATEMENT:
Write a program to Print repeated character pattern.
A
BB
CCC
DDDD
EEEEE
"""

def repeated_character_pattern(n):

    """To print the repeated character pattern, we can use a loop that iterates from 1 to n. 
       In each iteration, we print the corresponding character (starting from 'A') 
       repeated as many times as the iteration number itself.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(1, n + 1):
    
        print(chr(64 + i) * i)  # Print the character corresponding to i repeated i times

height = int(input("Enter the height of the repeated character pattern: "))

repeated_character_pattern(height)