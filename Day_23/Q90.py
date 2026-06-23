"""
PROBLEM STATEMENT:
Write a program to Find first repeating character.
"""

def first_repeating_char(s):

    """Finds the first character in a string that appears more than once.
       We use a set to keep track of characters we have already seen as we traverse the string.
       The time complexity of this approach is O(n), where n is the length of the string."""
    
    seen_chars = set()
    
    for char in s:
    
        if char in seen_chars:
        
            return char
            
        seen_chars.add(char)
        
    return None


try:

    user_input = input("Enter a string: ").strip()
    
    if not user_input:
    
        raise ValueError("The input string cannot be empty!")
        
    # Calculate and display the result
    
    result = first_repeating_char(user_input)
    
    if result:
    
        print(f"\nThe first repeating character is: '{result}'")
        
    else:
    
        print("\nNo repeating characters found in the string.")

except ValueError as e:

    print(f"Input Error: {e}")