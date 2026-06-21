"""
PROBLEM STATEMENT:
Write a program to Find string length without strlen().
"""

def string_len(input_string):

    """Calculates the length of a given string input_string without using the built-in len() function.
       We can iterate through each character of the string using a simple loop and increment a counter for every character encountered. 
       The loop naturally terminates when there are no more characters left in the string.
       The time complexity of this approach is O(n), where n is the number of characters in the string."""
    
    count = 0
    
    for char in input_string:
    
        count += 1
        
    return count

user_string = input("Enter a string: ")

length = string_len(user_string)

print(f"The length of the string is: {length}")