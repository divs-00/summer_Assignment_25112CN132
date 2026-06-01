"""
PROBLEM STATEMENT:
Write a program to Print repeated-number pattern.
1
22
333
4444
55555
"""

def repeated_number_pattern(n):

    """To print the repeated-number pattern, we can use a loop that iterates from 1 to n. 
       In each iteration, we print the current iteration number repeated as many times as the iteration number itself.
       The time complexity of this approach is O(n^2)."""
    
    for i in range(1, n + 1):
    
        print(str(i) * i)  # Print the current number i repeated i times

height = int(input("Enter the height of the repeated-number pattern: "))

repeated_number_pattern(height)