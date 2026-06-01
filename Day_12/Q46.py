"""
PROBLEM STATEMENT:
Write a program to Write function for Armstrong.
"""

def is_armstrong(num):

    """An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
       To check if a number is an Armstrong number, we can convert the number to a string to easily access each digit, 
       calculate the sum of the digits raised to the power of the number of digits, and compare it to the original number. 
       The time complexity of this approach is O(d), where d is the number of digits in the input number."""
    
    num_str = str(num)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == num

number = int(input("Enter a number: "))

if is_armstrong(number):

    print(f"{number} is an Armstrong number.")

else:

    print(f"{number} is not an Armstrong number.")