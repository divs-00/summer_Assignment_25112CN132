"""
PROBLEM STATEMENT:
Write a program to check whether a number is a palindrome or not.
"""

def is_palindrome(n):

    """Returns True if n is a palindrome, False otherwise.
       We can convert the number to a string and check if it reads the same forwards and backwards.
       This approach is efficient and works for both positive and negative numbers (negative numbers are not palindromes)."""
    
    s = str(n)
    
    return s == s[::-1]

num = int(input("Enter a number to check if it's a palindrome: "))

if is_palindrome(num):

    print(f"{num} is a palindrome.")

else:

    print(f"{num} is not a palindrome.")
