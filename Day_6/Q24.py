"""
PROBLEM STATEMENT:
Write a program to find x^n without pow().
"""

def power(x, n):

    """To calculate x raised to the power of n, we can use a simple loop to multiply x by itself n times. 
       If n is negative, we can calculate the positive power and then take the reciprocal. 
       The time complexity of this approach is O(n), where n is the exponent."""
    
    if n < 0:
    
        x = 1 / x
        
        n = -n
        
    result = 1
    
    for _ in range(n):
    
        result *= x
        
    return result

base = float(input("Enter the base (x): "))

exponent = int(input("Enter the exponent (n): "))

result = power(base, exponent)

print(f"{base} raised to the power of {exponent} is: {result}")