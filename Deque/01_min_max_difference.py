from collections import deque


def min_max_difference_sliding_window(arr, k):
    """
    Minimize the maximum difference by keeping n-k elements.

    Approach: Sort the array and use sliding window to find minimum max-min
    difference when keeping n-k elements.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if k >= len(arr) - 1:
        return 0

    arr.sort()
    n = len(arr)
    result = float("inf")

    for i in range(n - k):
        diff = arr[i + k] - arr[i]
        result = min(result, diff)

    return result


def min_max_difference_deque(arr, k):
    """
    Deque-based sliding window to minimize maximum difference.

    The problem: Given arr and k, minimize the maximum difference between
    adjacent elements by distributing k (adding to some elements).

    The minimum possible maximum difference is achieved when we can make
    all elements equal by distributing k appropriately.
    """
    if k == 0:
        return max(arr) - min(arr)

    arr.sort()
    n = len(arr)

    max_diff = arr[-1] - arr[0]

    dq = deque()
    for i in range(n):
        while dq and arr[i] - dq[0] > max_diff:
            dq.popleft()
        dq.append(arr[i])

    return max_diff


def main():
    print("=== Minimize Maximum Difference Between Adjacent Elements ===\n")

    test_cases = [
        ([3, 7, 8, 10, 14], 2, 6),
        ([12, 16, 22, 31, 31, 38], 3, 15),
        ([1, 5, 8, 10], 2, 4),
        ([4, 6], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
    ]

    print("--- Sliding Window Approach ---")
    for arr, k, expected in test_cases:
        result = min_max_difference_sliding_window(arr, k)
        status = "✓" if result == expected else "✗"
        print(f"arr = {arr}, k = {k} → {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    main()
