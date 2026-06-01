"""
PROBLEM STATEMENT:
Write a program to Rotate array right.
"""

def rotate_array_right(arr, positions):

    """Rotates the elements of the array arr to the right by a specified number of positions.
       This function takes an array and the number of positions to rotate as input, and returns a new array with the elements rotated to the right. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    if not arr:
    
        return arr  # Return empty array if input is empty
    
    positions = positions % len(arr)  # Handle cases where positions > length of array
    
    return arr[-positions:] + arr[:-positions]

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = input(f"Enter element {i + 1}: ")

    array.append(element)

positions = int(input("Enter the number of positions to rotate right: "))

rotated_array = rotate_array_right(array, positions)

print("Array after right rotation:", rotated_array)