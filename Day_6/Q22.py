"""
PROBLEM STATEMENT:
Write a program to convert binary to decimal.
"""

def binary_to_decimal(binary):

    """To convert a binary number to decimal, we can iterate through each digit of the binary number, 
       starting from the rightmost digit. 
       For each digit, we multiply it by 2 raised to the power of its position (starting from 0) and 
       sum these values to get the decimal representation. 
       The time complexity of this approach is O(d), where d is the number of digits in the binary number."""
    
    decimal = 0
    
    binary_str = str(binary)
    
    length = len(binary_str)
    
    for i in range(length):
    
        digit = int(binary_str[length - 1 - i])
        
        decimal += digit * (2 ** i)
        
    return decimal

binary_input = int(input("Enter a binary number: "))

decimal_result = binary_to_decimal(binary_input)

print(f"The decimal representation of {binary_input} is: {decimal_result}")