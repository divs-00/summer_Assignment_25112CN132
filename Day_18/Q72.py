"""
PROBLEM STATEMENT:
Write a program to Sort array in descending order.
"""

def sort_array_descending(arr):
    
    """Sorts the array arr in descending order.
       To sort an array in descending order, we can use the built-in sorted function with the reverse parameter set to True.
       The time complexity of this approach is O(n log n) due to the sorting algorithm used by the sorted function."""
    
    sorted_arr = sorted(arr, reverse=True)
    
    return sorted_arr

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to sort integers

    array.append(element)

sorted_array = sort_array_descending(array)

print("Array sorted in descending order:", sorted_array)