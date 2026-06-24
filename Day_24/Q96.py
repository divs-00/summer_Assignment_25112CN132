"""
PROBLEM STATEMENT:
Write a program to Remove duplicate characters.
"""

def remove_duplicate_characters(input_str):

    """Removes duplicate characters from a string while preserving the original order.
       This function utilizes a set to keep track of characters that have already been seen 
       and iterates through the string to build a list of unique characters.
       The time complexity of this approach is O(n), where n is the length of the string."""
    
    seen_characters = set()
    
    unique_chars = []
    
    for char in input_str:
    
        if char not in seen_characters:
        
            seen_characters.add(char)
            
            unique_chars.append(char)
            
    return "".join(unique_chars)

user_string = input("Enter a string: ")

result = remove_duplicate_characters(user_string)

print(f"String after removing duplicates: {result}")