"""
PROBLEM STATEMENT:
Write a program to Reverse a string.
"""

def reverse_string(s):

    """Reverses the given input string s.
       We can use Python's slicing method with a step of -1 to reverse the string efficiently. 
       This approach starts from the end of the string and moves backwards to the beginning. 
       The time complexity of this approach is O(n), where n is the length of the string, as it visits each character once."""
    
    return s[::-1]

input_string = input("Enter a string to reverse: ")

reversed_result = reverse_string(input_string)

print(f"The reversed string is: {reversed_result}")