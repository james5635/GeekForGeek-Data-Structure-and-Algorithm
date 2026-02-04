def pushZerosToEnd(arr):
    """
    Move all zeros to the end of array using two traversals.

    Time Complexity: O(n)
    Space Complexity: O(1)

    First Traversal: Shift non-zero elements to the front
    Second Traversal: Fill remaining positions with zeros

    Args:
        arr: List of integers
    """
    # Count of non-zero elements
    count = 0

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
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
