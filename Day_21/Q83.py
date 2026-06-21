"""
PROBLEM STATEMENT:
Write a program to Count vowels and consonants.
"""

def count_vowels_and_consonants(s):

    """Counts the number of vowels and consonants in the given string s.
       We can iterate through each character of the string, convert it to lowercase, and check if it is an alphabet letter. 
       If it is, we check if it belongs to a predefined set of vowels; if so, we increment the vowel count, otherwise we increment the consonant count. 
       The time complexity of this approach is O(n), where n is the length of the string, as we examine each character exactly once."""
    
    vowels = set("aeiou")
    
    vowel_count = 0
    
    consonant_count = 0
    
    for char in s:
    
        char_lower = char.lower()
        
        if char_lower.isalpha():
        
            if char_lower in vowels:
            
                vowel_count += 1
                
            else:
            
                consonant_count += 1
                
    return vowel_count, consonant_count

input_string = input("Enter a string: ")

vowels, consonants = count_vowels_and_consonants(input_string)

print(f"Number of vowels: {vowels}")

print(f"Number of consonants: {consonants}")