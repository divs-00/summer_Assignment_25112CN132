"""
PROBLEM STATEMENT:
Write a program to move zeroes to end.
"""

def move_zeroes_to_end(arr):

    """Moves all zeroes in the array arr to the end while maintaining the order of non-zero elements.
       This function takes an array as input and iterates through its elements, moving non-zero elements to the front and filling the rest with zeroes. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    non_zero_index = 0
    
    for i in range(len(arr)):
    
        if arr[i] != 0:
        
            arr[non_zero_index] = arr[i]
            
            non_zero_index += 1
            
    for i in range(non_zero_index, len(arr)):
    
        arr[i] = 0
        
    return arr

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to move zeroes for integers

    array.append(element)

result = move_zeroes_to_end(array)

print("Array after moving zeroes to the end:", result)