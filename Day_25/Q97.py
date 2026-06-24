"""
PROBLEM STATEMENT:
Write a program to Merge two sorted arrays.
"""

def merge_sorted_arrays(arr1, arr2):

    """Merges two already sorted arrays into a single sorted array.
       This function uses a two-pointer approach to compare elements from both arrays 
       and append the smaller element to the merged array, handling any remaining elements afterward.
       The time complexity of this approach is O(n + m), where n and m are the lengths of the two arrays."""
    
    merged_array = []
    
    i = 0
    
    j = 0
    
    while i < len(arr1) and j < len(arr2):
    
        if arr1[i] < arr2[j]:
        
            merged_array.append(arr1[i])
            
            i += 1
            
        else:
        
            merged_array.append(arr2[j])
            
            j += 1
            
    while i < len(arr1):
    
        merged_array.append(arr1[i])
        
        i += 1
        
    while j < len(arr2):
    
        merged_array.append(arr2[j])
        
        j += 1
        
    return merged_array

size1 = int(input("Enter the size of the first array: "))

array1 = []

for i in range(size1):

    element = int(input(f"Enter element {i + 1} for first array (sorted): "))

    array1.append(element)

size2 = int(input("Enter the size of the second array: "))

array2 = []

for i in range(size2):

    element = int(input(f"Enter element {i + 1} for second array (sorted): "))

    array2.append(element)

result = merge_sorted_arrays(array1, array2)

print(f"Merged sorted array: {result}")