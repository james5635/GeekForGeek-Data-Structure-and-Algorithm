def pushZerosToEnd(arr):
    """
    Move all zeros to the end of array using single traversal.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Uses two-pointer technique with swapping to move zeros to end
    while maintaining relative order of non-zero elements.

    Args:
        arr: List of integers
    """
    # Pointer to track the position for next non-zero element
    count = 0

    for i in range(len(arr)):
        # If the current element is non-zero
        if arr[i] != 0:
            # Swap the current element with the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]

            # Move 'count' pointer to the next position
            count += 1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 0, 4, 3, 0, 5, 0],
        [10, 20, 30],
        [0, 0],
        [0, 1, 0, 2, 0, 3],
        [1, 0, 2, 0, 3, 0],
        [],
    ]

    for arr in test_cases:
        original = arr.copy()
        pushZerosToEnd(arr)
        print(f"Input: {original}")
        print(f"Output: {arr}")
        print("-" * 40)
