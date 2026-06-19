"""
PROBLEM STATEMENT:
Write a program to Transpose matrix.
"""

def transpose(mat):

    """Transposes a matrix using pure Python built-ins.
       Time Complexity: O(Rows * Columns) - Moves every element exactly once."""
    
    if not mat or not mat[0]:
    
        return []
        
    # zip(*mat) pairs matching column items via highly optimized C code.
    # We map 'list' across it to output mutable lists instead of tuples.
    return list(map(list, zip(*mat)))

try:

    rows = int(input("Enter the number of rows for the matrix: "))

    print("Enter the elements of the matrix:")

    matrix = []

    expected_cols = None

    for i in range(rows):

        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        
        # Enforce valid matrix geometry

        if expected_cols is None:

            expected_cols = len(row)

        elif len(row) != expected_cols:

            raise ValueError("All rows must have the same number of columns!")
            
        matrix.append(row)

    result = transpose(matrix)

    print("\nResult of transposing the matrix:")

    for row in result:

        print(" ".join(map(str, row)))

except ValueError as e:

    print(f"Input Error: {e}")