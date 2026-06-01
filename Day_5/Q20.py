"""
PROBLEM STATEMENT:
Write a program to find largest prime factor.
"""

def largest_prime_factor(num):

    """The largest prime factor of a number is the greatest prime number that divides the number without leaving a remainder.
       To find the largest prime factor, we can start by dividing the number by the smallest prime (2) 
       and continue dividing by the next primes until we cannot divide anymore. 
       The last prime that successfully divides the number will be the largest prime factor. 
       The time complexity of this approach is O(sqrt(n)), where n is the input number."""
    
    largest_factor = None
    
    # Check for factors of 2
    while num % 2 == 0:
    
        largest_factor = 2
        
        num //= 2
        
    # Check for odd factors from 3 to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
    
        while num % i == 0:
        
            largest_factor = i
            
            num //= i
            
    # If num is a prime number greater than 2
    if num > 2:
    
        largest_factor = num
        
    return largest_factor

number = int(input("Enter a number: "))

result = largest_prime_factor(number)

if result is not None:

    print(f"The largest prime factor of {number} is: {result}")

else:

    print(f"{number} has no prime factors.")
