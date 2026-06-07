"""
PROBLEM STATEMENT:
Write a program to Remove duplicates from array.
"""

def remove_duplicates(arr):

    """Removes duplicate elements from the array arr while maintaining the order of first occurrences.
       We can use a set to keep track of seen elements and a list to store the unique elements. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    seen = set()
    
    unique_arr = []
    
    for num in arr:
    
        if num not in seen:
        
            unique_arr.append(num)
            
            seen.add(num)
            
    return unique_arr

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to remove duplicates for integers

    array.append(element)

result = remove_duplicates(array)

print("Array after removing duplicates:", result)