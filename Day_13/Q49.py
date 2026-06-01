"""
PROBLEM STATEMENT:
Write a program to input and display array.
"""

def display_array(arr):

    """Displays the elements of the array arr.
       This function takes an array as input and prints its elements in a readable format.
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    print("Array elements:", end=' ')
    
    for element in arr:
    
        print(element, end=' ')
        
    print()  # for a new line after displaying the array

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = input(f"Enter element {i + 1}: ")

    array.append(element)

display_array(array)