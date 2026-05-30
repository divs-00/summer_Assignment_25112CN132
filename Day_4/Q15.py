"""
PROBLEM STATEMENT:
Write a program to check Armstrong number.
"""

def is_armstrong(original_num):

    """Returns True if n is an Armstrong number, False otherwise.
       An Armstrong number is a number, 
       that is equal to the sum of its own digits each raised to the power of the number of digits.
       We can convert the number to a string to easily access each digit and calculate the sum. 
       The time complexity of this approach is O(d), where d is the number of digits in n."""
    
    number = str(original_num)
    
    num_digits = len(number)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in number)
    
    return armstrong_sum == original_num

num = int(input("Enter a number to check if it's an Armstrong number: "))

if is_armstrong(num):

    print(f"{num} is an Armstrong number.")

else:

    print(f"{num} is not an Armstrong number.")