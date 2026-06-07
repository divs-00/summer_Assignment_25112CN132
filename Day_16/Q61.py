"""
PROBLEM STATEMENT:
Write a program to Find missing number in array.
"""

def find_missing_number(arr, n):

    """Finds the missing number in an array of size n containing numbers from 1 to n with one number missing.
       We can calculate the expected sum of numbers from 1 to n using the formula n*(n+1)/2, and then subtract the actual sum of the elements in the array from this expected sum to find the missing number. 
       The time complexity of this approach is O(n), where n is the size of the array."""
    
    expected_sum = n * (n + 1) // 2
    
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum

size = int(input("Enter the size of the array (n): "))

array = []

for i in range(size - 1):  # Since one number is missing, we take size - 1

    element = int(input(f"Enter element {i + 1}: "))

    array.append(element)

missing_number = find_missing_number(array, size)

print(f"The missing number is: {missing_number}")