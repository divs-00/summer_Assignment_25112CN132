"""
PROBLEM STATEMENT:
Write a program to print factors of a number.
"""

def print_factors(num):

    """"
    Factors of a number are the integers that can be multiplied together to produce that number.
    To find the factors of a number, we can iterate from 1 to the half of the number and check if it divides the number evenly.
    The time complexity of this approach is O(n), where n is the input number."""
    
    factors = []
    
    for i in range(1, num // 2 + 1):
    
        if num % i == 0:
        
            factors.append(i)
            
    factors.append(num)  # The number itself is also a factor
    
    return factors

number = int(input("Enter a number: "))

print(f"Factors of {number} are: {print_factors(number)}")