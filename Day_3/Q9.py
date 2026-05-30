"""
PROBLEM STATEMENT:
Write a program to check whether a number is prime.
"""

def is_prime(n):
    
    """Returns True if n is a prime number, False otherwise.
       A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
       We can check for primality by testing divisibility from 2 up to the square root of n. 
       We can skip even numbers greater than 2 to optimize the check. 
       The time complexity of this approach is O(sqrt(n))."""
    
    if n <= 1:
    
        return False  # 0 and 1 are not prime numbers
    
    if n <= 3:
    
        return True  # 2 and 3 are prime numbers    
    
    for i in range(2, int(n**0.5) + 1, 2):

        if n % i == 0:

            return False  # n is divisible by a number other than 1 and itself
    
    return True  # n is a prime number

num = int(input("Enter a number to check if it's prime: "))

if is_prime(num):

    print(f"{num} is a prime number.")

else:

    print(f"{num} is not a prime number.")