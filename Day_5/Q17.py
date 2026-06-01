"""
PROBLEM STATEMENT:
Write a program to check perfect number.
"""

def is_perfect_number(num):

    """A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
       To check if a number is perfect, we can find all of its proper divisors and sum them up. 
       If the sum equals the original number, then it is a perfect number. 
       The time complexity of this approach is O(n), where n is the input number."""
    
    if num < 2:
    
        return False
    
    sum_of_divisors = 1  # Start with 1, which is a proper divisor of every number
    
    for i in range(2, num // 2 + 1):
    
        if num % i == 0:
    
            sum_of_divisors += i
            
    return sum_of_divisors == num

number = int(input("Enter a number: "))

if is_perfect_number(number):

    print(f"{number} is a perfect number.")

else:

    print(f"{number} is not a perfect number.")