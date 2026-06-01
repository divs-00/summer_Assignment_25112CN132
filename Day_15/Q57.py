"""
PROBLEM STATEMENT:
Write a program to Reverse array.
"""

def reverse_array(arr):

    """Reverses the elements of the array arr.
       This function takes an array as input and creates a new array with the elements in reverse order. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    reversed_arr = []
    
    for i in range(len(arr) - 1, -1, -1):
    
        reversed_arr.append(arr[i])
        
    return reversed_arr

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = input(f"Enter element {i + 1}: ")

    array.append(element)

reversed_array = reverse_array(array)

print("Reversed array:", reversed_array)