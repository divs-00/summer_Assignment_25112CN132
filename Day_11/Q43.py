"""
PROBLEM STATEMENT:
Write a program to Write function to check prime.
"""

def is_prime(num):

    """A prime number is a natural number greater than 1 
       that cannot be formed by multiplying two smaller natural numbers.
       To check if a number is prime, we can check if it is divisible by any integer 
       from 2 to the square root of the number.
       If it is divisible by any of those integers, then it is not a prime number. 
       The time complexity of this approach is O(sqrt(n)), where n is the input number."""
    
    if num <= 1:
    
        return False
    
    if num <= 3:
    
        return True
    
    if num % 2 == 0:
    
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
    
        if num % i == 0:
        
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):

    print(f"{number} is a prime number.")

else:

    print(f"{number} is not a prime number.")