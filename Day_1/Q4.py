"""
PROBLEM STATEMENT:
Write a program to count digits in a number.
"""

def count_digits(n):

    """Returns the count of digits in the number n.
       We can convert the number to a string and count its length, which is an efficient way to count digits.
       The time complexity of this approach is O(d), where d is the number of digits in n."""
    
    return len(str(abs(n)))  # Use abs to handle negative numbers

num = int(input("Enter a number to count its digits: "))

result = count_digits(num)

print(f"The number of digits in {num} is: {result}")