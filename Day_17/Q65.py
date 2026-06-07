"""
PROBLEM STATEMENT:
Write a program to Merge arrays.
"""

def merge_arrays(arr1, arr2):

    """Merges two arrays arr1 and arr2 into a single array.
       We can simply concatenate the two arrays using the + operator. 
       The time complexity of this approach is O(n + m), where n and m are the sizes of arr1 and arr2 respectively."""
    
    return arr1 + arr2

size1 = int(input("Enter the size of the first array: "))

array1 = []

for i in range(size1):

    element = int(input(f"Enter element {i + 1} of the first array: "))  # Assuming we want to merge arrays of integers

    array1.append(element)

size2 = int(input("Enter the size of the second array: "))

array2 = []

for i in range(size2):

    element = int(input(f"Enter element {i + 1} of the second array: "))  # Assuming we want to merge arrays of integers

    array2.append(element)

result = merge_arrays(array1, array2)

print("Merged array:", result)
