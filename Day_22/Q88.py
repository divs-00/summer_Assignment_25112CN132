"""
PROBLEM STATEMENT:
Write a program to Remove spaces from string.
"""

def remove_spaces(s):

    """Removes all whitespace characters from the given string s.
       We can use Python's built-in replace() method to replace all space characters with an empty string. 
       Alternatively, split() and join() can be used to handle all types of whitespace like tabs and newlines. 
       The time complexity of this approach is O(n), where n is the length of the string, as it processes each character to build the new string."""
    
    return s.replace(" ", "")

input_string = input("Enter a string with spaces: ")

result_string = remove_spaces(input_string)

print(f"The string without spaces is: {result_string}")