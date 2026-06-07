"""
PROBLEM STATEMENT:
Write a program to Find common elements.
"""

def find_common_elements(arr1, arr2):

    """Finds the common elements between two arrays arr1 and arr2.
       We can use a set to store the unique elements from one array, and then check for each element in the other array if it exists in the set. 
       The time complexity of this approach is O(n + m), where n and m are the sizes of arr1 and arr2 respectively."""
    
    set_arr1 = set(arr1)
    
    return [element for element in arr2 if element in set_arr1]

size1 = int(input("Enter the size of the first array: "))

array1 = []

for i in range(size1):

    element = int(input(f"Enter element {i + 1} of the first array: "))  # Assuming we want to find common elements for arrays of integers

    array1.append(element)

size2 = int(input("Enter the size of the second array: "))

array2 = []

for i in range(size2):

    element = int(input(f"Enter element {i + 1} of the second array: "))  # Assuming we want to find common elements for arrays of integers

    array2.append(element)

result = find_common_elements(array1, array2)

print("Common elements in the two arrays:", result)
