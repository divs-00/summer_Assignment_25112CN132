"""
PROBLEM STATEMENT:
Write a program to write function for perfect number.
"""

def is_perfect_number(n):

    """A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. 
       To check if a number is perfect, we can find all of its proper divisors and sum them up. 
       If the sum equals the original number, then it is a perfect number. 
       The time complexity of this approach is O(n) in the worst case, where n is the input number."""
    
    if n < 1:
        return False
    
    divisor_sum = 0
    
    for i in range(1, n):
    
        if n % i == 0:
        
            divisor_sum += i
            
    return divisor_sum == n

number = int(input("Enter a number: "))

if is_perfect_number(number):

    print(f"{number} is a perfect number.")

else:

    print(f"{number} is not a perfect number.")