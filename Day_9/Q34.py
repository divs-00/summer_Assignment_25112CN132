"""
PROBLEM STATEMENT:
Write a program to Print reverse number triangle.
12345
1234
123
12
1
"""

def reverse_number_triangle(n):

    """
    To print a reverse number triangle of height n, we can use a loop that iterates from n down to 1. 
    In each iteration, we print a substring of the string '123456789' that contains the first 'digit' characters, 
    where 'digit' is the current iteration number. 
    This way, we can efficiently generate the required pattern without needing to convert
    numbers to strings or perform additional calculations. 
    The time complexity of this approach is O(n^2)."""

    numbers = '123456789'  # A string containing digits from 1 to 9

    for digit in range(n, 0, -1):

        print(numbers[:digit])  # Print the substring of numbers from index 0 to digit

height = int(input("Enter the height of the reverse number triangle: "))

reverse_number_triangle(height)