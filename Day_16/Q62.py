"""
PROBLEM STATEMENT:
Write a program to Find maximum frequency element.
"""

def find_max_frequency_element(arr):

    """Finds the element with the maximum frequency in the array arr.
       We can use a dictionary to count the frequency of each element in the array, and then find the element with the highest frequency. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    frequency = {}
    
    for num in arr:
    
        if num in frequency:
        
            frequency[num] += 1
            
        else:
        
            frequency[num] = 1
            
    max_freq_element = max(frequency, key=frequency.get)
    
    return max_freq_element

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to find max frequency for integers

    array.append(element)

max_freq_element = find_max_frequency_element(array)

print(f"The element with the maximum frequency is: {max_freq_element}")