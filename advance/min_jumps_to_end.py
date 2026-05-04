"""
Minimum Number of Jumps to Reach End

Implements an algorithm to compute the minimum number of jumps required
to reach the last index of the array, where each element represents the
maximum jump length from that position. Uses greedy approach for optimal
time complexity.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def min_jumps_to_end(arr: list) -> int:
    """
    Compute minimum jumps to reach end of array.

    Args:
        arr: List of non-negative integers representing max jump length

    Returns:
        Minimum number of jumps, or -1 if end is unreachable
    """
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    max_reach = 0  # Farthest index reachable
    curr_end = 0  # End of current jump range
    jumps = 0  # Number of jumps taken

    for i in range(n):
        max_reach = max(max_reach, i + arr[i])

        # If we reach the end of current jump range
        if i == curr_end:
            # If we can't jump further
            if i == max_reach:
                return -1
            jumps += 1
            curr_end = max_reach

            # If we can reach the end, return jumps
            if curr_end >= n - 1:
                return jumps

    return -1


if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    result1 = min_jumps_to_end(arr1)
    print(f"Test 1 - Minimum jumps: {result1} (Expected: 3)")

    # Test case 2
    arr2 = [1, 4, 3, 2, 6, 7]
    result2 = min_jumps_to_end(arr2)
    print(f"Test 2 - Minimum jumps: {result2} (Expected: 2)")

    # Test case 3: Unreachable
    arr3 = [0, 10, 20]
    result3 = min_jumps_to_end(arr3)
    print(f"Test 3 - Minimum jumps: {result3} (Expected: -1)")
