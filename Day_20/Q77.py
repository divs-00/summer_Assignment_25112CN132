"""
PROBLEM STATEMENT:
Write a program to Multiply matrices.
"""

def multiply_matrices(matrix_a, matrix_b):

    """Multiplies two dimensions-compatible matrices matrix_a and matrix_b.
       We can transpose the second matrix to efficiently compute the dot product of rows and columns using list comprehensions and the sum function.
       The time complexity of this approach is O(m*n*p), where m and n are the dimensions of matrix_a, and n and p are the dimensions of matrix_b."""
    
    if not matrix_a or not matrix_b or len(matrix_a[0]) != len(matrix_b):
    
        raise ValueError("Incompatible matrix dimensions for multiplication.")
        
    cols_b = list(zip(*matrix_b))
    
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in cols_b] for row_a in matrix_a]
            
    return result

rows_a = int(input("Enter the number of rows for Matrix A: "))

cols_a = int(input("Enter the number of columns for Matrix A: "))

print("Enter the elements of the first matrix:")

matrix_a = []

for i in range(rows_a):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix_a.append(row)

rows_b = int(input("Enter the number of rows for Matrix B: "))

cols_b = int(input("Enter the number of columns for Matrix B: "))

if cols_a != rows_b:

    print(f"Error: Cannot multiply. Columns of A ({cols_a}) must match Rows of B ({rows_b}).")
    
    exit()

print("Enter the elements of the second matrix:")

matrix_b = []

for i in range(rows_b):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix_b.append(row)

result = multiply_matrices(matrix_a, matrix_b)

print("Result of multiplying the two matrices:")

for row in result:

    print(" ".join(map(str, row)))