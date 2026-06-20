"""
PROBLEM STATEMENT:
Write a program to Find column-wise sum.
"""

def find_column_wise_sum(matrix):

    """Calculates the sum of elements for each column in the matrix.
       We can unpack and zip the matrix to iterate through its columns as rows, computing the sum of each column using the built-in sum function.
       The time complexity of this approach is O(m*n), where m and n are the number of rows and columns in the matrix, respectively."""
    
    if not matrix:
    
        return []
        
    result = []
    
    for col in zip(*matrix):
    
        result.append(sum(col))
        
    return result

rows = int(input("Enter the number of rows for the matrix: "))

cols = int(input("Enter the number of columns for the matrix: "))

print("Enter the elements of the matrix:")

matrix = []

for i in range(rows):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix.append(row)

result = find_column_wise_sum(matrix)

print("Column-wise sum of the matrix:")

for idx, col_sum in enumerate(result):

    print(f"Sum of Column {idx + 1}: {col_sum}")