"""
PROBLEM STATEMENT:
Write a program to Linear search.
"""

def linear_search(arr, target):

    """Performs a linear search for the target element in the array arr.
       This function iterates through each element in the array and checks if it matches the target. 
       If a match is found, it returns the index of the target; otherwise, it returns -1 after checking all elements. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    for index in range(len(arr)):
    
        if arr[index] == target:
        
            return index
            
    return -1  # Target not found

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = input(f"Enter element {i + 1}: ")

    array.append(element)

target = input("Enter the element to search for: ")

result = linear_search(array, target)

if result != -1:

    print(f'Element "{target}" found at index: {result}')

else:

    print(f'Element "{target}" not found in the array.')