"""
PROBLEM STATEMENT:
Write a program to recursive sum of digits.
"""

def recursive_sum_of_digits(n):

    """Returns the sum of digits in the number n using recursion.
       We can define the base case for n = 0, where the sum of digits is 0. 
       For n > 0, we can take the last digit (n % 10) and add it to the sum of digits of the remaining number (n // 10). 
       The time complexity of this approach is O(d), where d is the number of digits in n."""
    
    if n == 0:
    
        return 0
        
    else:
    
        return (n % 10) + recursive_sum_of_digits(n // 10)
    
num = int(input("Enter a number to find the recursive sum of its digits: "))

result = recursive_sum_of_digits(num)

print(f"The recursive sum of digits in {num} is: {result}")