"""
PROBLEM STATEMENT:
Write a program to Convert lowercase to uppercase.
"""

def convert_to_uppercase(s):

    """Converts all lowercase characters in the given string s to uppercase.
       We can iterate through each character, check if its ASCII value falls within the lowercase range, and convert it by shifting its ASCII value, or use Python's built-in upper() method. 
       Using the built-in method provides an optimized and clean implementation. 
       The time complexity of this approach is O(n), where n is the length of the string, as each character is processed once."""
    
    return s.upper()

input_string = input("Enter a string in lowercase: ")

uppercase_result = convert_to_uppercase(input_string)

print(f"The uppercase string is: {uppercase_result}")