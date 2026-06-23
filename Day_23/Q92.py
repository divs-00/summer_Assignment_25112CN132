"""
PROBLEM STATEMENT:
Write a program to Find maximum occurring character.
"""

def max_occurring_char(s):

    """Finds the character that appears most frequently in a string.
       We use a frequency dictionary to count occurrences and keep track of the maximum count seen so far.
       The time complexity of this approach is O(n), where n is the length of the string."""
    
    char_count = {}
    
    max_char = None
    
    max_count = 0
    
    for char in s:
    
        char_count[char] = char_count.get(char, 0) + 1
        
        # Track the character with the maximum frequency
        
        if char_count[char] > max_count:
        
            max_count = char_count[char]
            
            max_char = char
            
    return max_char, max_count


try:

    user_input = input("Enter a string: ")
    
    if not user_input:
    
        raise ValueError("The input string cannot be empty!")
        
    # Calculate and display the result
    
    result_char, result_count = max_occurring_char(user_input)
    
    if result_char:
    
        print(f"\nThe maximum occurring character is: '{result_char}' (occurs {result_count} times)")
        
    else:
    
        print("\nNo character found.")

except ValueError as e:

    print(f"Input Error: {e}")