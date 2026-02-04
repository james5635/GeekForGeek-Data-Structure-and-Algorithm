"""
Maximum Consecutive 1s with K Flips

Find maximum consecutive 1s after flipping at most k 0s.

Approaches:
1. Naive: Try all windows - O(n²) time, O(1) space
2. Optimal: Sliding Window - O(n) time, O(1) space
"""


def max_consecutive_ones_naive(arr, k):
    """
    Naive approach: Try all possible subarrays.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting index, extend window
    - Count zeros in window
    - If zeros <= k, update max length

    Args:
        arr: Binary array (0s and 1s)
        k: Maximum number of 0s that can be flipped

    Returns:
        Maximum length of consecutive 1s after at most k flips
    """
    n = len(arr)
    max_len = 0

    for i in range(n):
        zeros = 0
        for j in range(i, n):
            if arr[j] == 0:
                zeros += 1

            if zeros <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break

    return max_len


def max_consecutive_ones_sliding_window(arr, k):
    """
    Optimal approach: Sliding Window.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Use two pointers (left and right) for window
    - Expand window by moving right pointer
    - Count zeros in window
    - If zeros > k, shrink window from left
    - Track maximum window size

    Key Insight:
    We want the longest window with at most k zeros.
    This is equivalent to finding longest subarray where
    we can flip k zeros to make all 1s.

    Args:
        arr: Binary array (0s and 1s)
        k: Maximum number of 0s that can be flipped

    Returns:
        Maximum length of consecutive 1s after at most k flips
    """
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(arr)):
        # Expand window
        if arr[right] == 0:
            zeros += 1

        # Shrink window if zeros exceed k
        while zeros > k:
            if arr[left] == 0:
                zeros -= 1
            left += 1

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len


def max_consecutive_ones_with_positions(arr, k):
    """
    Sliding window that also returns which zeros to flip.

    Returns:
        Tuple of (max_length, start_index, zero_positions_to_flip)
    """
    left = 0
    zeros = 0
    max_len = 0
    best_left = 0
    zero_positions = []

    for right in range(len(arr)):
        if arr[right] == 0:
            zeros += 1
            zero_positions.append(right)

        while zeros > k:
            if arr[left] == 0:
                zeros -= 1
                zero_positions.remove(left)
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_left = left

    return max_len, best_left, zero_positions[:k]


def max_consecutive_ones_queue(arr, k):
    """
    Alternative using queue to track zero positions.

    Time Complexity: O(n)
    Space Complexity: O(k)

    Algorithm:
    - Use queue to store positions of zeros in current window
    - When queue size exceeds k, move left to after first zero
    """
    from collections import deque

    zero_queue = deque()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        if arr[right] == 0:
            zero_queue.append(right)

        # If more than k zeros, shrink from left
        if len(zero_queue) > k:
            left = zero_queue.popleft() + 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),  # Output: 6
        ([1, 1, 0, 0, 1, 1, 1, 0, 1, 1], 1),  # Output: 5
        ([1, 1, 1, 1], 0),  # Output: 4
        ([0, 0, 0, 0], 2),  # Output: 2
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),  # Output: 10
        ([1], 0),  # Output: 1
        ([0], 1),  # Output: 1
        ([], 2),  # Output: 0
    ]

    print("=" * 70)
    print("Maximum Consecutive 1s with K Flips")
    print("=" * 70)
    print("\nFind maximum consecutive 1s after flipping at most k 0s.\n")

    for i, (arr, k) in enumerate(test_cases, 1):
        naive = max_consecutive_ones_naive(arr, k)
        sliding = max_consecutive_ones_sliding_window(arr, k)
        queue = max_consecutive_ones_queue(arr, k)

        match = naive == sliding == queue

        print(f"Test {i}: arr = {arr}, k = {k}")
        print(f"  Naive O(n²):          {naive}")
        print(f"  Sliding Window O(n):  {sliding}")
        print(f"  Queue O(n):           {queue} {'✓' if match else '✗'}")

        # Show which zeros to flip
        if arr:
            result = max_consecutive_ones_with_positions(arr, k)
            print(f"  Best window:          arr[{result[1]}:{result[1] + result[0]}]")
            print(f"  Flip zeros at:        {result[2]}")
        print()

    print("=" * 70)
    print("\nSliding Window Explanation:")
    print("  - Expand window by moving right pointer")
    print("  - Count zeros in window")
    print("  - If zeros > k, shrink from left until zeros <= k")
    print("  - Track maximum window size")
    print("\n  This finds the longest subarray with at most k zeros.")
    print("  Flipping those k zeros gives us consecutive 1s.")
    print("=" * 70)
