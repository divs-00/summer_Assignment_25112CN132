"""
PROBLEM STATEMENT:
Write a program to count even and odd elements.
"""

def count_even_and_odd(arr):

    """Counts the number of even and odd elements in the array arr.
       This function takes an array as input and iterates through its elements to count how many are even and how many are odd. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    even_count = 0
    
    odd_count = 0
    
    for element in arr:
    
        if isinstance(element, int):  # Check if the element is an integer
        
            if element % 2 == 0:
            
                even_count += 1
                
            else:
            
                odd_count += 1
                
    return even_count, odd_count

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to count even and odd for integers

    array.append(element)

even_count, odd_count = count_even_and_odd(array)

print(f"The number of even elements in the array is: {even_count}")

print(f"The number of odd elements in the array is: {odd_count}")