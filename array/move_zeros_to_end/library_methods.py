def pushZerosToEndLibrary(arr):
    """
    Move all zeros to the end of array using Python library methods.

    Time Complexity: O(n)
    Space Complexity: O(n) due to list comprehension

    Uses list comprehension and list concatenation to achieve the result.

    Args:
        arr: List of integers
    Returns:
        List with zeros moved to the end
    """
    # Separate non-zero elements and zeros
    non_zero = [x for x in arr if x != 0]
    zeros = [x for x in arr if x == 0]

    # Concatenate non-zero elements with zeros
    return non_zero + zeros


def pushZerosToEndSort(arr):
    """
    Move all zeros to the end of array using sort with custom key.

    Time Complexity: O(n log n)
    Space Complexity: O(n) for sort operation

    Args:
        arr: List of integers
    Returns:
        List with zeros moved to the end
    """
    # Sort with key that puts zeros at the end
    return sorted(arr, key=lambda x: x == 0)


def pushZerosToEndFilter(arr):
    """
    Move all zeros to the end of array using filter function.

    Time Complexity: O(n)
    Space Complexity: O(n) due to filter and concatenation

    Args:
        arr: List of integers
    Returns:
        List with zeros moved to the end
    """
    # Use filter to get non-zero elements
    non_zero = list(filter(lambda x: x != 0, arr))
    zeros = list(filter(lambda x: x == 0, arr))

    return non_zero + zeros


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

    methods = [
        ("List Comprehension", pushZerosToEndLibrary),
        ("Sort with Key", pushZerosToEndSort),
        ("Filter Function", pushZerosToEndFilter),
    ]

    for method_name, method in methods:
        print(f"=== {method_name} Method ===")
        for arr in test_cases:
            original = arr.copy()
            result = method(arr)
            print(f"Input: {original}")
            print(f"Output: {result}")
            print("-" * 40)
        print("\n")
