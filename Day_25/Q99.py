"""
PROBLEM STATEMENT:
Write a program to Sort names alphabetically.
"""

def sort_names_alphabetically(names_list):

    """Sorts a list of names in alphabetical order.
       This function takes a list of strings and uses Python's built-in sorting 
       mechanism to arrange them alphabetically in a case-insensitive manner.
       The time complexity of this approach is O(n * log(n) * m), where n is the number of names and m is the average length of a name."""
    
    sorted_list = sorted(names_list, key=str.lower)
    
    return sorted_list

size = int(input("Enter the number of names: "))

names_array = []

for i in range(size):

    name = input(f"Enter name {i + 1}: ")

    names_array.append(name)

result = sort_names_alphabetically(names_array)

print(f"Names in alphabetical order: {result}")