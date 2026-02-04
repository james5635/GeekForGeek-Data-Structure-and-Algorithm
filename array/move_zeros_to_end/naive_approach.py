def pushZerosToEnd(arr):
    """
    Move all zeros to the end of array using temporary array.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        arr: List of integers
    """
    n = len(arr)
    temp = [0] * n

    # to keep track of the index in temp[]
    j = 0

    # Copy non-zero elements to temp[]
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Fill remaining positions in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # Copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]


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
