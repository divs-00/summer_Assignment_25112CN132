"""
PROBLEM STATEMENT:
Write a program to Find row-wise sum.
"""

def find_row_wise_sum(matrix):

    """Calculates the sum of elements for each row in the matrix.
       We can iterate through each row of the matrix, compute the sum of its elements using Python's built-in sum function, and store it in a list.
       The time complexity of this approach is O(m*n), where m and n are the number of rows and columns in the matrix, respectively."""
    
    result = []
    
    for row in matrix:
    
        result.append(sum(row))
        
    return result

rows = int(input("Enter the number of rows for the matrix: "))

cols = int(input("Enter the number of columns for the matrix: "))

print("Enter the elements of the matrix:")

matrix = []

for i in range(rows):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix.append(row)

result = find_row_wise_sum(matrix)

print("Row-wise sum of the matrix:")

for idx, row_sum in enumerate(result):

    print(f"Sum of Row {idx + 1}: {row_sum}")