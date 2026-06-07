"""
PROBLEM STATEMENT:
Write a program to Union of arrays.
"""

def union_of_arrays(arr1, arr2):

    """Finds the union of two arrays arr1 and arr2.
       We can use a set to store the unique elements from both arrays, and then convert the set back to a list. 
       The time complexity of this approach is O(n + m), where n and m are the sizes of arr1 and arr2 respectively."""
    
    return list(set(arr1) | set(arr2))

size1 = int(input("Enter the size of the first array: "))

array1 = []

for i in range(size1):

    element = int(input(f"Enter element {i + 1} of the first array: "))  # Assuming we want to find union for arrays of integers

    array1.append(element)

size2 = int(input("Enter the size of the second array: "))

array2 = []

for i in range(size2):

    element = int(input(f"Enter element {i + 1} of the second array: "))  # Assuming we want to find union for arrays of integers

    array2.append(element)

result = union_of_arrays(array1, array2)

print("Union of the two arrays:", result)