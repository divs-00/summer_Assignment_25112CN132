"""
PROBLEM STATEMENT:
Write a program to find Second largest element.
"""

def find_second_largest(arr):

    """Finds the second largest element in an array.
       This function takes an array as input and iterates through its elements to find the largest and second largest values. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    if len(arr) < 2:
    
        return None  # Return None if there are less than 2 elements
    
    largest = second_largest = float('-inf')  # Initialize to negative infinity
    
    for element in arr:
    
        if element > largest:
        
            second_largest = largest
            
            largest = element
            
        elif largest > element > second_largest:
        
            second_largest = element
            
    return second_largest

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = float(input(f"Enter element {i + 1}: "))  # Assuming we want to find second largest for numbers

    array.append(element)

second_largest = find_second_largest(array)

if second_largest is not None:

    print(f"The second largest element in the array is: {second_largest}")

else:

    print("There is no second largest element in the array.")