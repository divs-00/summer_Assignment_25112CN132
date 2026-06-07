"""
PROBLEM STATEMENT:
Write a program to Bubble sort.
"""

def bubble_sort(arr):

    """Sorts the array arr using the bubble sort algorithm.
       Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. 
       The time complexity of this approach is O(n^2) in the worst and average cases, and O(n) in the best case when the array is already sorted."""
    
    n = len(arr)
    
    for i in range(n):
    
        for j in range(0, n - i - 1):
        
            if arr[j] > arr[j + 1]:
            
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to sort integers

    array.append(element)

sorted_array = bubble_sort(array)

print("Array after bubble sort:", sorted_array)