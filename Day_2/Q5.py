"""
PROBLEM STATEMENT:
Write a program to find sum of digits of a number.
"""

def sum_of_digits(n):

    """Returns the sum of digits in the number n.
       We can convert the number to a string, iterate through each character, 
       convert it back to an integer, and sum them up.
       Here, we use list comprehension to make the code concise and efficient.
       The time complexity of this approach is O(d), where d is the number of digits in n."""
    
    return sum(int(digit) for digit in str(abs(n)))  # Use abs to handle negative numbers

num = int(input("Enter a number to find the sum of its digits: "))

result = sum_of_digits(num)

print(f"The sum of digits in {num} is: {result}")