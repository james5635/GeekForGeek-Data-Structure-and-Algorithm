"""
Find Duplicate Rows in a Binary Matrix

Given a binary matrix, print the rows which are duplicates of rows
that are already present in the matrix. Returns 1-based indices of
duplicate rows.

Approach: Use a hash set to store string representations of each row.
If a row string is already in the set, its index is added to the result.

Time Complexity: O(m * n) where m is number of rows and n is number of columns
Auxiliary Space: O(m * n)

Source: https://www.geeksforgeeks.org/dsa/find-duplicate-rows-binary-matrix/
"""


def repeated_rows(matrix):
    """Find duplicate rows in a binary matrix.

    Args:
        matrix: A 2D list of binary values (0s and 1s).

    Returns:
        A list of 1-based indices of duplicate rows.
    """
    result = []
    seen = set()

    for i, row in enumerate(matrix):
        row_str = "".join(map(str, row))
        if row_str in seen:
            result.append(i + 1)
        else:
            seen.add(row_str)

    return result


def repeated_rows_zero_based(matrix):
    """Find duplicate rows in a binary matrix (0-based indices).

    Args:
        matrix: A 2D list of binary values (0s and 1s).

    Returns:
        A list of 0-based indices of duplicate rows.
    """
    result = []
    seen = set()

    for i, row in enumerate(matrix):
        row_str = "".join(map(str, row))
        if row_str in seen:
            result.append(i)
        else:
            seen.add(row_str)

    return result


def repeated_rows_trie(matrix):
    """Find duplicate rows using a Trie data structure.

    Args:
        matrix: A 2D list of binary values (0s and 1s).

    Returns:
        A list of 1-based indices of duplicate rows.
    """

    class TrieNode:
        def __init__(self):
            self.children = [None, None]
            self.is_leaf = False

    def insert(head, row):
        curr = head
        for val in row:
            if curr.children[val] is None:
                curr.children[val] = TrieNode()
            curr = curr.children[val]
        if curr.is_leaf:
            return False
        curr.is_leaf = True
        return True

    result = []
    head = TrieNode()

    for i, row in enumerate(matrix):
        if not insert(head, row):
            result.append(i + 1)

    return result


if __name__ == "__main__":
    print("Test Case 1:")
    mat1 = [
        [1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
    ]
    print("Input matrix:")
    for i, row in enumerate(mat1):
        print(f"  Row {i + 1}: {row}")
    duplicates = repeated_rows(mat1)
    print(f"Duplicate rows (1-based indices): {duplicates}")

    print("\nTest Case 2 (no duplicates):")
    mat2 = [
        [0, 1, 0],
        [1, 0, 1],
        [1, 1, 0],
    ]
    print("Input matrix:")
    for i, row in enumerate(mat2):
        print(f"  Row {i + 1}: {row}")
    duplicates = repeated_rows(mat2)
    print(f"Duplicate rows: {duplicates}")

    print("\nTest Case 3 (Trie approach):")
    mat3 = [
        [1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
    ]
    duplicates_trie = repeated_rows_trie(mat3)
    print(f"Duplicate rows using Trie (1-based indices): {duplicates_trie}")
