"""
PROBLEM STATEMENT:
Write a program to find Frequency of an element.
"""

def frequency_of_element(arr, element):

    """Counts the frequency of a specific element in the array arr.
       This function takes an array and an element as input 
       and iterates through the array to count how many times the specified element appears. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    count = 0
    
    for item in arr:
    
        if item == element:
        
            count += 1
            
    return count

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = input(f"Enter element {i + 1}: ")

    array.append(element)

target = input("Enter the element to find the frequency of: ")

frequency = frequency_of_element(array, target)

print(f'Frequency of "{target}" in the array is: {frequency}')