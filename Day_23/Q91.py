"""
PROBLEM STATEMENT:
Write a program to Check anagram strings.
"""

def is_anagram(s1, s2):

    """Checks if two strings are anagrams of each other.
       We first remove whitespace and convert to lowercase, then check if their sorted characters match.
       The time complexity of this approach is O(n log n), where n is the length of the strings."""
    
    # Clean the strings by removing spaces and converting to lowercase
    
    clean_s1 = s1.replace(" ", "").lower()
    
    clean_s2 = s2.replace(" ", "").lower()
    
    # Anagrams must have the same length after cleaning
    
    if len(clean_s1) != len(clean_s2):
    
        return False
        
    return sorted(clean_s1) == sorted(clean_s2)


try:

    str1 = input("Enter the first string: ")
    
    str2 = input("Enter the second string: ")
    
    if not str1.strip() or not str2.strip():
    
        raise ValueError("Both input strings must contain characters!")
        
    # Calculate and display the result
    
    if is_anagram(str1, str2):
    
        print(f"\n'{str1}' and '{str2}' are anagrams.")
        
    else:
    
        print(f"\n'{str1}' and '{str2}' are not anagrams.")

except ValueError as e:

    print(f"Input Error: {e}")