"""
Reorder Array According to Given Indexes

Given two arrays: arr[] and index[] of same size N.
Reorder arr[] according to given index[] array.

Approaches:
1. Naive: O(n²) with extra space - Create new array using index mapping
2. Optimal: O(n) in-place - Use swapping to place elements at correct positions
"""


def reorder_naive(arr, index):
    """
    Naive approach: Create new array using index mapping.

    Time Complexity: O(n²) - due to searching for next index
    Space Complexity: O(n) - for result array

    Algorithm:
    - Create a new array of same size
    - Place each element arr[i] at position index[i] in new array
    - Return new array

    Args:
        arr: List of elements to reorder
        index: List of target indices for each element

    Returns:
        Reordered array
    """
    n = len(arr)
    result = [None] * n

    for i in range(n):
        result[index[i]] = arr[i]

    return result


def reorder_naive_sorted(arr, index):
    """
    Better Naive: Sort pairs by index, then extract.

    Time Complexity: O(n log n) - for sorting
    Space Complexity: O(n) - for pairs and result

    Algorithm:
    - Create pairs of (index[i], arr[i])
    - Sort pairs by index
    - Extract arr values in sorted order

    Args:
        arr: List of elements to reorder
        index: List of target indices

    Returns:
        Reordered array
    """
    n = len(arr)

    # Create pairs and sort by index
    pairs = [(index[i], arr[i]) for i in range(n)]
    pairs.sort(key=lambda x: x[0])

    # Extract values in order
    return [pair[1] for pair in pairs]


def reorder_optimal_inplace(arr, index):
    """
    Optimal approach: In-place reordering using cyclic swapping.

    Time Complexity: O(n²) in worst case, O(n) average
    Space Complexity: O(1) - modifies arrays in-place

    Algorithm:
    - For each position i, check if index[i] == i
    - If not, swap arr[i] with arr[index[i]] and index[i] with index[index[i]]
    - Repeat until element at position i is at correct index

    Args:
        arr: List of elements (modified in-place)
        index: List of indices (modified in-place)

    Returns:
        Tuple of (reordered array, updated index array)
    """
    n = len(arr)

    for i in range(n):
        # While current element is not at its correct position
        while index[i] != i:
            # Swap arr[i] with arr[index[i]]
            # Swap index[i] with index[index[i]]
            target_idx = index[i]

            # Swap elements
            arr[i], arr[target_idx] = arr[target_idx], arr[i]

            # Swap indices
            index[i], index[target_idx] = index[target_idx], index[i]

    return arr, index


def reorder_optimal_extra_space(arr, index):
    """
    Optimal approach with O(n) space: Position elements directly.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Create a copy of arr
    - Place each element at its target position using index mapping
    - Copy back to original array

    Args:
        arr: List of elements
        index: List of target indices

    Returns:
        Reordered array
    """
    n = len(arr)
    temp = arr.copy()

    for i in range(n):
        arr[index[i]] = temp[i]

    return arr


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (arr, index, expected_arr, expected_index)
        ([50, 40, 70, 60, 90], [3, 0, 4, 1, 2], [40, 60, 90, 50, 70], [0, 1, 2, 3, 4]),
        ([10, 11, 12], [1, 0, 2], [11, 10, 12], [0, 1, 2]),
        (
            ["a", "b", "c", "d", "e"],
            [4, 3, 2, 1, 0],
            ["e", "d", "c", "b", "a"],
            [0, 1, 2, 3, 4],
        ),
        ([1], [0], [1], [0]),
        ([1, 2], [1, 0], [2, 1], [0, 1]),
    ]

    print("=" * 70)
    print("Reorder Array According to Given Indexes")
    print("=" * 70)

    for i, (arr, index, expected_arr, expected_index) in enumerate(test_cases, 1):
        # Test naive
        result_naive = reorder_naive(arr.copy(), index.copy())

        # Test naive sorted
        result_sorted = reorder_naive_sorted(arr.copy(), index.copy())

        # Test optimal with extra space
        arr_copy = arr.copy()
        index_copy = index.copy()
        result_optimal_space = reorder_optimal_extra_space(arr_copy, index_copy)

        # Test optimal in-place
        arr_copy2 = arr.copy()
        index_copy2 = index.copy()
        result_inplace, final_index = reorder_optimal_inplace(arr_copy2, index_copy2)

        print(f"\nTest {i}:")
        print(f"  Original arr:   {arr}")
        print(f"  Original index: {index}")
        print(f"  Expected arr:   {expected_arr}")
        print(f"  Expected index: {expected_index}")
        print(
            f"  Naive O(n²):         {result_naive} {'✓' if result_naive == expected_arr else '✗'}"
        )
        print(
            f"  Sorted O(n log n):   {result_sorted} {'✓' if result_sorted == expected_arr else '✗'}"
        )
        print(
            f"  Optimal O(n) space:  {result_optimal_space} {'✓' if result_optimal_space == expected_arr else '✗'}"
        )
        print(
            f"  Optimal O(1) space:  {result_inplace} {'✓' if result_inplace == expected_arr else '✗'}"
        )

    print("\n" + "=" * 70)
    print("\nAlgorithm Explanation:")
    print("\n1. Naive Approach O(n²):")
    print("   - Create new array of size n")
    print("   - Place arr[i] at position index[i] in new array")
    print("   - Time: O(n), Space: O(n)")
    print("\n2. Better Naive O(n log n):")
    print("   - Create pairs of (index[i], arr[i])")
    print("   - Sort pairs by index")
    print("   - Extract arr values")
    print("   - Time: O(n log n), Space: O(n)")
    print("\n3. Optimal In-place O(n):")
    print("   - For each position i:")
    print("     - While index[i] ≠ i:")
    print("       - Swap arr[i] with arr[index[i]]")
    print("       - Swap index[i] with index[index[i]]")
    print("   - Each element swapped at most once")
    print("   - Time: O(n), Space: O(1)")
    print("\nKey Insight: Follow the index chain until element is at correct position")
    print("=" * 70)
