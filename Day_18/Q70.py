"""
PROBLEM STATEMENT:
Write a program to Selection sort.
"""

def selection_sort(arr):

    """Sorts the array arr using the selection sort algorithm.
       Selection sort is a simple sorting algorithm that divides the input list into two parts: 
       the sorted part at the left end and the unsorted part at the right end. 
       The algorithm repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part. 
       The time complexity of this approach is O(n^2) in all cases, as it requires two nested loops to complete the sorting process."""
    
    n = len(arr)
    
    for i in range(n):
    
        min_index = i
        
        for j in range(i + 1, n):
        
            if arr[j] < arr[min_index]:
            
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to sort integers

    array.append(element)

sorted_array = selection_sort(array)

print("Array after selection sort:", sorted_array)