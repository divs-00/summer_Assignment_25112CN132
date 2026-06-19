"""
PROBLEM STATEMENT:
Write a program to Find diagonal sum.
"""

def diagonal_sum(mat):

    """Calculates the sum of the diagonal in a matrix. The diagonals in a square matrix have equal index of both rows and columns.
       So, we only need a single for loop for this operation.
       The time complexity of this approach is O(n), where n is the number of elements in the array"""
    
    size = len(mat)
    
    total_sum = 0
    
    for i in range(n):
    
        total_sum += mat[i][i]
        
    return total_sum


try:
    
    n = int(input("Enter the size of the square matrix (N x N): "))
    
    print(f"Enter the elements of the {n}x{n} matrix:")

    matrix = []

    for i in range(n):
    
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        
        # Enforce that the matrix is perfectly square
    
        if len(row) != n:
    
            raise ValueError(f"Row {i + 1} must have exactly {n} elements to be a square matrix!")
            
        matrix.append(row)

    # Calculate and display the sum
    
    result = diagonal_sum(matrix)
    
    print(f"\nThe sum of the primary diagonal is: {result}")

except ValueError as e:
    
    print(f"Input Error: {e}")
