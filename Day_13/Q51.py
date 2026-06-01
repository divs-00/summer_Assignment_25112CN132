"""
PROBLEM STATEMENT:
Write a program to find largest and smallest element.
"""

def find_largest_and_smallest(arr):

    """Finds the largest and smallest elements in an array.
       This function takes an array as input and iterates through its elements to find the maximum and minimum values. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    if not arr:
    
        return None, None  # Return None for both if the array is empty
    
    largest = smallest = arr[0]  # Initialize largest and smallest to the first element
    
    for element in arr:
    
        if element > largest:
        
            largest = element
            
        elif element < smallest:
        
            smallest = element
            
    return largest, smallest

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = float(input(f"Enter element {i + 1}: "))  # Assuming we want to find largest and smallest for numbers

    array.append(element)

largest, smallest = find_largest_and_smallest(array)

print(f"The largest element in the array is: {largest}")

print(f"The smallest element in the array is: {smallest}")