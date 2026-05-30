"""
PROBLEM STATEMENT:
Write a program to find the GCD of two numbers.
"""

def gcd(a, b):

    """Returns the greatest common divisor (GCD) of a and b using the Euclidean algorithm.
       The time complexity of this algorithm is O(log(min(a, b))).
       The Euclidean algorithm is efficient for finding the GCD and works by repeatedly replacing 
       the larger number with the remainder of the division until one of the numbers becomes zero. 
       The non-zero number at that point will be the GCD."""
    
    while b:
    
        a, b = b, a % b
    
    return abs(a)  # Return the absolute value to handle negative numbers

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")