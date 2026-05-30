"""
PROBLEM STATEMENT:
Write a program to reverse a number.
"""

def reverse_number(n):

    """Returns the reverse of the number n.
       We can convert the number to a string, reverse it, and convert it back to an integer.
       This approach is efficient and handles both positive and negative numbers correctly."""
    
    sign = -1 if n < 0 else 1

    n = abs(n)
    
    reversed_str = str(n)[::-1]
    
    return sign * int(reversed_str)

num = int(input("Enter a number to reverse: "))

result = reverse_number(num)

print(f"The reverse of {num} is: {result}")