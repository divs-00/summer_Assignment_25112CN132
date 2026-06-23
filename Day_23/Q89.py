"""
PROBLEM STATEMENT:
Write a program to Find first non-repeating character.
"""

def first_non_repeating_char(s):

    """Finds the first character in a string that does not repeat anywhere else. 
       We use a frequency dictionary to count occurrences in the first pass, then find the first character with a count of 1.
       The time complexity of this approach is O(n), where n is the length of the string."""
    
    char_count = {}
    
    # First pass: Count the frequency of each character
    
    for char in s:
    
        char_count[char] = char_count.get(char, 0) + 1
        
    # Second pass: Find the first character with a frequency of 1
    
    for char in s:
    
        if char_count[char] == 1:
        
            return char
            
    return None


try:

    user_input = input("Enter a string: ").strip()
    
    if not user_input:
    
        raise ValueError("The input string cannot be empty!")
        
    # Calculate and display the result
    
    result = first_non_repeating_char(user_input)
    
    if result:
    
        print(f"\nThe first non-repeating character is: '{result}'")
        
    else:
    
        print("\nAll characters repeat or no unique character found.")

except ValueError as e:

    print(f"Input Error: {e}")