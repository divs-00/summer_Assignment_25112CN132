"""
PROBLEM STATEMENT:
Write a program to Write function for palindrome.
"""

def is_palindrome(s):

    """A palindrome is a word, phrase, number, or other sequence of characters 
       that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). 
       To check if a string is a palindrome, we can remove non-alphanumeric characters 
       and convert the string to lowercase. Then we can compare the cleaned string with its reverse. 
       The time complexity of this approach is O(n), where n is the length of the input string."""
    
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):

    print(f'"{input_string}" is a palindrome.')

else:

    print(f'"{input_string}" is not a palindrome.')