"""
PROBLEM STATEMENT:
Write a program to Subtract matrices.
"""

def subtract_matrices(matrix_a, matrix_b):

    """Subtracts two matrices matrix_a and matrix_b of the same dimensions.
       We can iterate through each element of the matrices, subtract the corresponding elements, and store the result in a new matrix. 
       The time complexity of this approach is O(m*n), where m and n are the number of rows and columns in the matrices, respectively."""
    
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
    
        raise ValueError("Matrices must have the same dimensions for subtraction.")
        
    result = [[0 for _ in range(len(matrix_a[0]))] for _ in range(len(matrix_a))]
    
    for i in range(len(matrix_a)):
    
        for j in range(len(matrix_a[0])):
        
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
            
    return result

rows = int(input("Enter the number of rows for the matrices: "))

cols = int(input("Enter the number of columns for the matrices: "))

print("Enter the elements of the first matrix:")

matrix_a = []

for i in range(rows):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix_a.append(row)

print("Enter the elements of the second matrix:")

matrix_b = []

for i in range(rows):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix_b.append(row)

result = subtract_matrices(matrix_a, matrix_b)

print("Result of subtracting the two matrices:")

for row in result:

    print(" ".join(map(str, row)))