"""
PROBLEM STATEMENT:
Write a program to find duplicates in array.
"""

def find_duplicates(arr):

    """Finds duplicate elements in the array arr.
       This function takes an array as input and uses a set to track seen elements. 
       If an element is already in the set, it is added to the duplicates set. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    seen = set()
    
    duplicates = set()
    
    for element in arr:
    
        if element in seen:
        
            duplicates.add(element)
            
        else:
        
            seen.add(element)
            
    return duplicates

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = input(f"Enter element {i + 1}: ")

    array.append(element)

duplicates = find_duplicates(array)

if duplicates:

    print("Duplicate elements in the array are:", duplicates)

else:

    print("No duplicate elements found in the array.")