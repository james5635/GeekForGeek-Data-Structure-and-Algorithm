"""
Minimum XOR Value Pair

Implements an algorithm to find the minimum XOR value of any pair
in the array. Sorts the array and checks consecutive pairs, as the
minimum XOR must occur between adjacent elements in the sorted array.

Time Complexity: O(n log n)
Space Complexity: O(1) (excluding input storage)
"""


def find_min_xor_pair(arr: list) -> int:
    """
    Find the minimum XOR value of any pair in the array.

    Args:
        arr: List of integers

    Returns:
        Minimum XOR value of any pair
    """
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")

    # Sort the array
    sorted_arr = sorted(arr)
    min_xor = float("inf")

    # Check consecutive pairs (minimum XOR is between adjacent elements)
    for i in range(len(sorted_arr) - 1):
        current_xor = sorted_arr[i] ^ sorted_arr[i + 1]
        if current_xor < min_xor:
            min_xor = current_xor

    return min_xor


if __name__ == "__main__":
    # Test case 1
    arr1 = [9, 5, 3]
    result1 = find_min_xor_pair(arr1)
    print(f"Test 1 - Minimum XOR value: {result1} (Expected: 6)")

    # Test case 2
    arr2 = [1, 2, 3, 4, 5]
    result2 = find_min_xor_pair(arr2)
    print(f"Test 2 - Minimum XOR value: {result2} (Expected: 1)")

    # Test case 3
    arr3 = [1, 8, 3, 10]
    result3 = find_min_xor_pair(arr3)
    print(f"Test 3 - Minimum XOR value: {result3} (Expected: 2)")
