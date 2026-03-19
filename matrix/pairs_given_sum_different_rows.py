def find_pairs_given_sum_different_rows(matrix, target_sum):
    """
    Find pairs with given sum such that elements of pair are in different rows.

    Args:
        matrix: 2D list of integers
        target_sum: Target sum for pairs

    Returns:
        List of tuples representing pairs (value1, value2) where value1 and value2
        are from different rows and their sum equals target_sum
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Create a dictionary to store elements and their row indices
    # We'll store for each value, the set of rows where it appears
    value_rows = {}

    # Populate the dictionary
    for i in range(rows):
        for j in range(cols):
            val = matrix[i][j]
            if val not in value_rows:
                value_rows[val] = set()
            value_rows[val].add(i)

    # For each element, look for complement in different rows
    for i in range(rows):
        for j in range(cols):
            val = matrix[i][j]
            complement = target_sum - val

            if complement in value_rows:
                # Check if there's at least one occurrence of complement in a different row
                complement_rows = value_rows[complement]
                # If complement is same as val, we need at least two different rows
                if complement == val:
                    if len(complement_rows) > 1 or (
                        len(complement_rows) == 1 and i not in complement_rows
                    ):
                        # Actually, if complement == val, we need the value to appear in at least one different row
                        if any(row != i for row in complement_rows):
                            result.append((val, complement))
                else:
                    # If complement is different, we just need it to appear in any row different from i
                    if any(row != i for row in complement_rows):
                        result.append((val, complement))

    # Remove duplicates (since we might count (a,b) and (b,a) as different)
    # Sort each pair and use set to remove duplicates
    unique_pairs = set()
    for pair in result:
        sorted_pair = tuple(sorted(pair))
        unique_pairs.add(sorted_pair)

    # Convert back to list of tuples
    return [tuple(pair) for pair in unique_pairs]


def find_pairs_given_sum_different_rows_brute_force(matrix, target_sum):
    """
    Brute force approach for verification.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Check all pairs of elements from different rows
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(rows):
                # Skip same row
                if i2 == i1:
                    continue
                for j2 in range(cols):
                    if matrix[i1][j1] + matrix[i2][j2] == target_sum:
                        # Sort to avoid duplicates like (a,b) and (b,a)
                        pair = tuple(sorted([matrix[i1][j1], matrix[i2][j2]]))
                        result.append(pair)

    # Remove duplicates
    return list(set(result))


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Example matrix
    print("Test 1: Example matrix")
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    target_sum1 = 11

    print("Matrix:")
    print_matrix(matrix1)
    print(f"Target sum: {target_sum1}")

    result1 = find_pairs_given_sum_different_rows(matrix1, target_sum1)
    result1_brute = find_pairs_given_sum_different_rows_brute_force(
        matrix1, target_sum1
    )

    print(f"Pairs with sum {target_sum1} (optimized): {sorted(result1)}")
    print(f"Pairs with sum {target_sum1} (brute force): {sorted(result1_brute)}")
    print(f"Match: {sorted(result1) == sorted(result1_brute)}")
    print()

    # Test case 2: Duplicate values
    print("Test 2: Matrix with duplicate values")
    matrix2 = [[1, 1, 2], [2, 3, 1], [1, 2, 2]]
    target_sum2 = 3

    print("Matrix:")
    print_matrix(matrix2)
    print(f"Target sum: {target_sum2}")

    result2 = find_pairs_given_sum_different_rows(matrix2, target_sum2)
    result2_brute = find_pairs_given_sum_different_rows_brute_force(
        matrix2, target_sum2
    )

    print(f"Pairs with sum {target_sum2} (optimized): {sorted(result2)}")
    print(f"Pairs with sum {target_sum2} (brute force): {sorted(result2_brute)}")
    print(f"Match: {sorted(result2) == sorted(result2_brute)}")
    print()

    # Test case 3: No pairs
    print("Test 3: No pairs")
    matrix3 = [[1, 2], [3, 4]]
    target_sum3 = 20

    print("Matrix:")
    print_matrix(matrix3)
    print(f"Target sum: {target_sum3}")

    result3 = find_pairs_given_sum_different_rows(matrix3, target_sum3)
    result3_brute = find_pairs_given_sum_different_rows_brute_force(
        matrix3, target_sum3
    )

    print(f"Pairs with sum {target_sum3} (optimized): {sorted(result3)}")
    print(f"Pairs with sum {target_sum3} (brute force): {sorted(result3_brute)}")
    print(f"Match: {sorted(result3) == sorted(result3_brute)}")
    print()
