"""
PROBLEM STATEMENT:
Write a program to Find pair with given sum.
"""

def find_pair_with_sum(arr, target_sum):

    """Finds a pair of numbers in the array arr that add up to target_sum.
       We can use a set to keep track of the numbers we have seen so far while iterating through the array. 
       For each number, we check if the complement (target_sum - current number) exists in the set. 
       If it does, we have found a pair that adds up to target_sum. 
       The time complexity of this approach is O(n), where n is the number of elements in the array."""
    
    seen = set()
    
    for num in arr:
    
        complement = target_sum - num
        
        if complement in seen:
        
            return (complement, num)
            
        seen.add(num)
        
    return None  # Return None if no pair is found

size = int(input("Enter the size of the array: "))

array = []

for i in range(size):

    element = int(input(f"Enter element {i + 1}: "))  # Assuming we want to find pairs for integers

    array.append(element)

target_sum = int(input("Enter the target sum: "))

pair = find_pair_with_sum(array, target_sum)

if pair:

    print(f"A pair that adds up to {target_sum} is: {pair[0]} and {pair[1]}")

else:

    print(f"No pair found that adds up to {target_sum}.")