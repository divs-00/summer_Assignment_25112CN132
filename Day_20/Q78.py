"""
PROBLEM STATEMENT:
Write a program to Check symmetric matrix.
"""

def is_symmetric(matrix):

    """Checks if a square matrix is symmetric.
       We can compare each element at index (i, j) with its corresponding element at (j, i) to ensure they are identical.
       The time complexity of this approach is O(n^2), where n is the number of rows and columns in the square matrix."""
    
    # A symmetric matrix must be square
    if not matrix or len(matrix) != len(matrix[0]):
    
        return False
        
    n = len(matrix)
    
    for i in range(n):
    
        for j in range(i + 1, n):
        
            if matrix[i][j] != matrix[j][i]:
            
                return False
                
    return True

rows = int(input("Enter the number of rows for the matrix: "))

cols = int(input("Enter the number of columns for the matrix: "))

if rows != cols:

    print("A symmetric matrix must be square (rows must equal columns). The matrix is not symmetric.")
    
    exit()

print("Enter the elements of the matrix:")

matrix = []

for i in range(rows):

    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))

    matrix.append(row)

result = is_symmetric(matrix)

if result:

    print("The matrix is symmetric.")

else:

    print("The matrix is not symmetric.")