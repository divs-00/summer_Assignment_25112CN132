"""
PROBLEM STATEMENT:
Write a program to Binary search.
"""

def binary_search(arr, target):

    """Performs binary search on a sorted array arr to find the index of the target element.
       Binary search works by repeatedly dividing the search interval in half. If the target value is less than the middle element, we continue searching in the left half; if it's greater, we continue in the right half. 
       The time complexity of binary search is O(log n), where n is the number of elements in the array."""
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
    
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
        
            return mid
            
        elif arr[mid] < target:
        
            left = mid + 1
            
        else:
        
            right = mid - 1
            
    return -1  # Return -1 if target is not found

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to search for integers

    array.append(element)

target = int(input("Enter the target element to search for: "))

# Ensure the array is sorted before performing binary search
array.sort()

result = binary_search(array, target)

if result != -1:
    
    print(f"Element found at index {result}")

else:

    print("Element not found in the array")