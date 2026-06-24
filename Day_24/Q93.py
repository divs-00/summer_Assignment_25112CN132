"""
PROBLEM STATEMENT:
Write a program to Check string rotation.
"""

def is_string_rotation(str1, str2):

    """Checks if str2 is a rotation of str1.
       This function ensures both strings are of equal length and not empty, 
       then checks if str2 is a substring of str1 concatenated with itself.
       The time complexity of this approach is O(n), where n is the length of the string."""
    
    if len(str1) != len(str2) or not str1:
    
        return False
        
    combined_string = str1 + str1
    
    return str2 in combined_string

string1 = input("Enter the first string: ")

string2 = input("Enter the second string: ")

if is_string_rotation(string1, string2):

    print(f'"{string2}" is a rotation of "{string1}"')

else:

    print(f'"{string2}" is not a rotation of "{string1}"')