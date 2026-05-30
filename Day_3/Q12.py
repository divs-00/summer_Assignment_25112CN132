"""
PROBLEM STATEMENT:
Write a program to find LCM of two numbers.
"""


from Day_3.Q11 import gcd

def lcm(a, b):

    """Returns the least common multiple (LCM) of a and b.
       We can use the relationship between GCD and LCM: LCM(a, b) = abs(a * b) // GCD(a, b).
       This approach is efficient and works well for large numbers."""
    
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

result = lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is: {result}")