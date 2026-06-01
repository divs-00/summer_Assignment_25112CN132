"""
PROBLEM STATEMENT:
Write a program to find sum and average of array.
"""

def sum_and_average(arr):

    """Calculates the sum and average of the elements in the array arr.
       This function takes an array as input, computes the sum of its elements, 
       and then calculates the average by dividing the sum by the number of elements. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    total_sum = sum(arr)
    
    average = total_sum / len(arr) if arr else 0  # Avoid division by zero
    
    return total_sum, average

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = float(input(f"Enter element {i + 1}: "))  # Assuming we want to calculate sum and average for numbers

    array.append(element)

total_sum, average = sum_and_average(array)

print(f"The sum of the array is: {total_sum}")

print(f"The average of the array is: {average}")