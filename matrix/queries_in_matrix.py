def matrix_queries(matrix, queries):
    """
    Process queries on a matrix.
    This implementation handles two types of queries:
    1. Update query: Update value at a specific position
    2. Sum query: Calculate sum of elements in a submatrix

    Uses a 2D Binary Indexed Tree (Fenwick Tree) for efficient updates and queries.

    Args:
        matrix: 2D list of integers
        queries: List of queries, where each query is a list:
                [1, row, col, new_val] for update (1-indexed or 0-indexed based on implementation)
                [2, row1, col1, row2, col2] for sum query (returns sum of submatrix from (row1,col1) to (row2,col2))

    Returns:
        List of results for sum queries
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])

    # Create BIT (Binary Indexed Tree) - 1-indexed
    bit = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Helper function to update BIT
    def update_bit(row, col, delta):
        i = row
        while i <= rows:
            j = col
            while j <= cols:
                bit[i][j] += delta
                j += j & -j
            i += i & -i

    # Helper function to get prefix sum from (1,1) to (row,col)
    def query_bit(row, col):
        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += bit[i][j]
                j -= j & -j
            i -= i & -i
        return result

    # Initialize BIT with matrix values
    for i in range(rows):
        for j in range(cols):
            update_bit(i + 1, j + 1, matrix[i][j])

    results = []

    # Process queries
    for query in queries:
        if query[0] == 1:  # Update query: [1, row, col, new_val]
            _, row, col, new_val = query
            # Assuming 0-indexed input for row, col
            old_val = matrix[row][col]
            delta = new_val - old_val
            matrix[row][col] = new_val
            update_bit(row + 1, col + 1, delta)
        elif query[0] == 2:  # Sum query: [2, row1, col1, row2, col2]
            _, row1, col1, row2, col2 = query
            # Assuming 0-indexed input for coordinates
            # Convert to 1-indexed for BIT
            total = (
                query_bit(row2 + 1, col2 + 1)
                - query_bit(row1, col2 + 1)
                - query_bit(row2 + 1, col1)
                + query_bit(row1, col1)
            )
            results.append(total)

    return results


def matrix_queries_simple(matrix, queries):
    """
    Simple implementation of matrix queries without optimization.
    Good for small matrices or few queries.

    Args:
        matrix: 2D list of integers
        queries: List of queries:
                [1, row, col, new_val] for update
                [2, row1, col1, row2, col2] for sum query

    Returns:
        List of results for sum queries
    """
    if not matrix or not matrix[0]:
        return []

    results = []
    # Make a copy to avoid modifying original
    mat = [row[:] for row in matrix]

    for query in queries:
        if query[0] == 1:  # Update query
            _, row, col, new_val = query
            mat[row][col] = new_val
        elif query[0] == 2:  # Sum query
            _, row1, col1, row2, col2 = query
            total = 0
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    total += mat[i][j]
            results.append(total)

    return results


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic operations
    print("Test 1: Basic matrix queries")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original matrix:")
    print_matrix(matrix1)

    queries1 = [
        [2, 0, 0, 1, 1],  # Sum of submatrix from (0,0) to (1,1): 1+2+4+5 = 12
        [1, 1, 1, 10],  # Update matrix[1][1] to 10
        [2, 0, 0, 2, 2],  # Sum of entire matrix: 1+2+3+4+10+6+7+8+9 = 50
        [2, 1, 1, 2, 2],  # Sum of submatrix from (1,1) to (2,2): 10+6+8+9 = 33
    ]

    print("Processing queries:", queries1)
    results1 = matrix_queries(matrix1, queries1)
    print("Results (optimized):", results1)
    print("Matrix after queries:")
    print_matrix(matrix1)

    # Reset matrix for simple version test
    matrix1_simple = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    results1_simple = matrix_queries_simple(matrix1_simple, queries1)
    print("Results (simple):", results1_simple)
    print()

    # Test case 2: Larger matrix
    print("Test 2: Larger matrix")
    matrix2 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print("Original matrix:")
    print_matrix(matrix2)

    queries2 = [
        [2, 0, 0, 3, 3],  # Sum of entire matrix
        [1, 2, 2, 100],  # Update center element
        [2, 1, 1, 2, 2],  # Sum of 2x2 submatrix around center
    ]

    print("Processing queries:", queries2)
    results2 = matrix_queries(matrix2, queries2)
    print("Results (optimized):", results2)
    print("Matrix after queries:")
    print_matrix(matrix2)

    # Reset matrix for simple version test
    matrix2_simple = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    results2_simple = matrix_queries_simple(matrix2_simple, queries2)
    print("Results (simple):", results2_simple)
    print()
