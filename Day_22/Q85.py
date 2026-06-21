"""
PROBLEM STATEMENT:
Write a program to Check palindrome string.
"""

def is_palindrome(s):

    """Checks whether the given string s is a palindrome.
       We can normalize the string by removing any non-alphanumeric characters and converting it to lowercase, then compare it to its reverse. 
       If the string reads the same forwards and backwards, it is a palindrome. 
       The time complexity of this approach is O(n), where n is the length of the string, due to the filtering and reversal operations."""
    
    # Normalize the string by keeping only alphanumeric characters and lowering the case
    cleaned_string = "".join(char.lower() for char in s if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a string to check: ")

if is_palindrome(input_string):

    print("The string is a palindrome.")

else:

    print("The string is not a palindrome.")