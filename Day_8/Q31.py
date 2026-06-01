"""
PROBLEM STATEMENT:
Write a program to Print character triangle.
A
AB
ABC
ABCD
ABCDE
"""

def character_triangle(n):

    """
    Prints a character triangle of height n. Here, we can use a loop that iterates from 1 to n. 
    In each iteration, we print characters starting from 'A' up to the character corresponding to the current iteration number. 
    We can achieve this by using the ASCII values of the characters. 
    The ASCII value of 'A' is 65, 
    so we can calculate the ASCII value for the current character by adding the iteration number to 64 (since we start from 1).
    The time complexity of this approach is O(n^2)."""

    for i in range(1, n + 1):

        for j in range(65, 65 + i):  # Loop from ASCII value of 'A' to the current character

            print(chr(j), end='')  # Print the character corresponding to the ASCII value

        print()  # Move to the next line after each row

height = int(input("Enter the height of the character triangle: "))

character_triangle(height)