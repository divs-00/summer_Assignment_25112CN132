"""
PROBLEM STATEMENT:
Write a program to count set bits in a number.
"""

def count_set_bits(num):

    """To count the number of set bits (1s) in the binary representation of a number, 
       we can use the bitwise AND operation to check each bit of the number. 
       We can repeatedly right shift the number and count how many times we encounter a set bit. 
       The time complexity of this approach is O(log n), where n is the input number."""
    
    count = 0
    
    while num > 0:
    
        count += num & 1  # Increment count if the least significant bit is 1
        
        num >>= 1  # Right shift the bits to check the next bit
        
    return count

number = int(input("Enter a number: "))

set_bits_count = count_set_bits(number)

print(f"The number of set bits in {number} is: {set_bits_count}")