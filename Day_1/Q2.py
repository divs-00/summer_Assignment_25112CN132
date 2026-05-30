"""
PROBLEM STATEMENT:
Write a program to print the multiplication table of a given number.
"""

def multiplication_table(n, limit=10):

    """Prints the multiplication table of n up to n * limit (default is 10)."""
    
    for i in range(1, limit + 1):
    
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number to see its multiplication table: "))

multiplication_table(num)