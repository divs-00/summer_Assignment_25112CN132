"""
PROBLEM STATEMENT:
Write a program to convert decimal to binary.
"""

def decimal_to_binary(num):

    """To convert a decimal number to binary, we can repeatedly divide the number by 2 and keep track of the remainders. 
       The binary representation is formed by the remainders read in reverse order. 
       The time complexity of this approach is O(log n), where n is the input number."""
    
    if num == 0:
    
        return int("0")
    
    binary = ""
    
    while num > 0:
    
        remainder = num % 2
        
        binary = str(remainder) + binary
        
        num //= 2
        
    return int(binary)

number = int(input("Enter a decimal number: "))

binary_result = decimal_to_binary(number)

print(f"The binary representation of {number} is: {binary_result}")