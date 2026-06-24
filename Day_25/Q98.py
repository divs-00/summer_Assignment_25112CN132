"""
PROBLEM STATEMENT:
Write a program to Find common characters in strings.
"""

def find_common_characters(arr):

    """Finds all common characters that appear in all strings of a given array (including duplicates).
       This function initializes a frequency counter using the first string, then intersects it 
       with the character frequencies of every subsequent string to find the minimum common occurrences.
       The time complexity of this approach is O(n * m), where n is the number of strings and m is the average length of the strings."""
    
    if not arr:
    
        return []
        
    from collections import Counter
    
    common_counts = Counter(arr[0])
    
    for i in range(1, len(arr)):
    
        current_counts = Counter(arr[i])
        
        for char in list(common_counts.keys()):
        
            if char in current_counts:
            
                common_counts[char] = min(common_counts[char], current_counts[char])
                
            else:
            
                del common_counts[char]
                
    result_chars = []
    
    for char, count in common_counts.items():
    
        for j in range(count):
        
            result_chars.append(char)
            
    return result_chars

size = int(input("Enter the number of strings: "))

strings_array = []

for i in range(size):

    string_element = input(f"Enter string {i + 1}: ")

    strings_array.append(string_element)

result = find_common_characters(strings_array)

print(f"Common characters found: {result}")