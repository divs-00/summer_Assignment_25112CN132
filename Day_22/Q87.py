"""
PROBLEM STATEMENT:
Write a program to Character frequency.
"""

def character_frequency(s):

    """Calculates the frequency of each character in the given string s.
       We can use a dictionary to store the characters as keys and their respective counts as values. 
       We iterate through the string, and for each character, we increment its count in the dictionary. 
       The time complexity of this approach is O(n), where n is the length of the string, because we process each character exactly once."""
    
    frequency_dict = {}
    
    for char in s:
    
        if char in frequency_dict:
        
            frequency_dict[char] += 1
            
        else:
        
            frequency_dict[char] = 1
            
    return frequency_dict

input_string = input("Enter a string: ")

frequencies = character_frequency(input_string)

print("Character frequencies:")

for char, count in frequencies.items():

    print(f"'{char}': {count}")