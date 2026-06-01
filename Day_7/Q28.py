"""
PROBLEM STATEMENT:
Write a program to recursive reverse number.
"""

def recursive_reverse_number(n, rev=0):

    """Returns the reverse of the number n using recursion.
       We can define the base case for n = 0, where the reverse is 0. 
       For n > 0, we can take the last digit (n % 10) and add it to rev multiplied by 10, 
       then call the function recursively with n // 10. 
       The time complexity of this approach is O(d), where d is the number of digits in n."""
    
    if n == 0:
    
        return rev
        
    else:
    
        rev = rev * 10 + (n % 10)
        
        return recursive_reverse_number(n // 10, rev)

num = int(input("Enter a number to find its reverse: "))

result = recursive_reverse_number(num)

print(f"The reverse of {num} is: {result}")