"""
PROBLEM STATEMENT:
Write a program to pring strong numbers.
"""

def is_strong_number(num):

    """A strong number is a number whose sum of the factorial of its digits is equal to the number itself.
       To check if a number is a strong number, 
       we can calculate the factorial of each digit and sum them up. 
       If the sum equals the original number, then it is a strong number. 
       The time complexity of this approach is O(d), where d is the number of digits in the input number."""
    
    def factorial(n):
    
        if n == 0 or n == 1:
        
            return 1
            
        else:
        
            return n * factorial(n - 1)
    
    sum_of_factorials = 0
    
    temp = num
    
    while temp > 0:
    
        digit = temp % 10
        
        sum_of_factorials += factorial(digit)
        
        temp //= 10
        
    return sum_of_factorials == num

number = int(input("Enter a number: "))

if is_strong_number(number):

    print(f"{number} is a strong number.")

else:

    print(f"{number} is not a strong number.")