"""
PROBLEM STATEMENT:
Write a program to Compress a string.
"""

def compress_string(input_str):

    """Compresses a string by replacing consecutive duplicate characters with their count.
       This function iterates through the input string, counts consecutive identical characters,
       and appends the character and count to a list. If the compressed version is not shorter, 
       it returns the original string.
       The time complexity of this approach is O(n), where n is the length of the string."""
    
    if not input_str:
    
        return input_str
        
    compressed_chars = []
    
    current_char = input_str[0]
    
    count = 1
    
    for i in range(1, len(input_str)):
    
        if input_str[i] == current_char:
        
            count += 1
            
        else:
        
            compressed_chars.append(current_char + str(count))
            
            current_char = input_str[i]
            
            count = 1
            
    compressed_chars.append(current_char + str(count))
    
    compressed_str = "".join(compressed_chars)
    
    if len(compressed_str) < len(input_str):
    
        return compressed_str
        
    else:
    
        return input_str

user_string = input("Enter a string to compress: ")

result = compress_string(user_string)

print(f"Compressed string: {result}")