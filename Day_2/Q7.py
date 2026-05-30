"""
PROBLEM STATEMENT:
Write a program to find product of digits.
"""

def product_of_digits(n):

    """Returns the product of digits in the number n.
       We can convert the number to a string, iterate through each character, 
       convert it back to an integer, and multiply them together.
       Here, we use list comprehension to make the code concise and efficient.
       The time complexity of this approach is O(d), where d is the number of digits in n."""
    
    product = 1

    for digit in str(abs(n)):  # Use abs to handle negative numbers

        product *= int(digit)
    
    return product

num = int(input("Enter a number to find the product of its digits: "))

result = product_of_digits(num)

print(f"The product of digits in {num} is: {result}")