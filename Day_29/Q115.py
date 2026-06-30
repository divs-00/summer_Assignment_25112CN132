"""
PROBLEM STATEMENT:
Write a program to Create menu-driven string operations system.
"""

class StringOperations:

    """Performs diverse operations on text strings.
       This utility class encapsulates core manipulation routines including reversals,
       palindrome verification, substring discovery, and character counting analytics.
       The time complexities are: Reversal O(n), Palindrome O(n), and Counting O(n)."""

    def reverse_string(self, input_str):
    
        """Reverses the provided sequence of characters.
           The time complexity is O(n), where n is the length of the string."""
           
        return input_str[::-1]


    def check_palindrome(self, input_str):
    
        """Determines if a string reads the same backward as forward.
           Normalizes casing and strips spaces to ensure semantic accuracy."""
           
        cleaned = "".join(input_str.split()).lower()
        
        return cleaned == cleaned[::-1]


    def count_vowels_and_consonants(self, input_str):
    
        """Counts total numeric occurrences of vowel versus consonant letters.
           Ignores spaces, numeric digits, and individual special symbols."""
           
        vowels = "aeiou"
        
        v_count = 0
        
        c_count = 0
        
        for char in input_str.lower():
        
            if char.isalpha():
            
                if char in vowels:
                
                    v_count += 1
                    
                else:
                
                    c_count += 1
                    
        return v_count, c_count


    def find_substring(self, main_str, sub_str):
    
        """Searches for the first index location matching a target substring block.
           Returns the index if found, or negative one if it does not exist."""
           
        return main_str.find(sub_str)


string_tool = StringOperations()

while True:

    print("\n==============================")
    
    print("   STRING OPERATIONS SYSTEM")
    
    print("==============================")
    
    print("1. Reverse a String")
    
    print("2. Check for Palindrome")
    
    print("3. Count Vowels and Consonants")
    
    print("4. Find Substring Index")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "5":
    
        print("\nClosing string analytics toolkit. Goodbye!")
        
        break
        
    if choice in ("1", "2", "3", "4"):
    
        user_text = input("Enter your target string: ")
        
        if choice == "1":
        
            result = string_tool.reverse_string(user_text)
            
            print(f"\nOriginal: {user_text}")
            
            print(f"Reversed: {result}")
            
        elif choice == "2":
        
            if string_tool.check_palindrome(user_text):
            
                print(f"\nSuccess: '{user_text}' is a valid palindrome!")
                
            else:
            
                print(f"\nResult: '{user_text}' is not a palindrome.")
                
        elif choice == "3":
        
            vowels, consonants = string_tool.count_vowels_and_consonants(user_text)
            
            print(f"\nAnalysis for: '{user_text}'")
            
            print(f"Vowels Count: {vowels}")
            
            print(f"Consonants Count: {consonants}")
            
        elif choice == "4":
        
            target_sub = input("Enter substring to search for: ")
            
            idx = string_tool.find_substring(user_text, target_sub)
            
            if idx != -1:
            
                print(f"\nSubstring found! First matching index occurs at position: {idx}")
                
            else:
            
                print(f"\nSubstring '{target_sub}' was not found within the input string.")
                
    else:
    
        print("\nInvalid choice. Please provide a relative option number between 1 and 5.")