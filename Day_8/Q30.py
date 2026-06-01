"""
PROBLEM STATEMENT:
Write a program to Print number triangle.
1
12
123
1234
12345
"""

def number_triangle(n):
    
    """
    Prints a number triangle of height n. Here, we can use a loop that iterates from 1 to n. 
    In each iteration, we print a substring of the string '123456789' that contains the first 'digit' characters, 
    where 'digit' is the current iteration number. 
    This way, we can efficiently generate the required pattern without needing to convert
    numbers to strings or perform additional calculations. 
    The time complexity of this approach is O(n^2)."""

    numbers = '123456789'  # A string containing digits from 1 to 9

    for digit in range(1, n + 1):

        print(numbers[:digit])  # Print the substring of numbers from index 0 to digit

height = int(input("Enter the height of the number triangle: "))

number_triangle(height)