"""
Longest subarray with absolute difference between min and max ≤ X
Uses sliding window with min and max deques to maintain O(n) time complexity
"""

from collections import deque


def longest_subarray_diff(arr, x):
    if not arr:
        return []

    n = len(arr)
    max_len = 0
    best_start = 0

    min_deque = deque()
    max_deque = deque()
    start = 0

    for end in range(n):
        while min_deque and arr[end] <= arr[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(end)

        while max_deque and arr[end] >= arr[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(end)

        while arr[max_deque[0]] - arr[min_deque[0]] > x:
            start += 1
            if min_deque[0] < start:
                min_deque.popleft()
            if max_deque[0] < start:
                max_deque.popleft()

        current_len = end - start + 1
        if current_len > max_len:
            max_len = current_len
            best_start = start

    return arr[best_start : best_start + max_len]


def main():
    print("=" * 60)
    print("Longest Subarray with Absolute Difference ≤ X")
    print("=" * 60)

    print("\n--- Test Case 1 ---")
    arr = [8, 4, 5, 6, 7]
    x = 3
    result = longest_subarray_diff(arr, x)
    print(f"Input: arr = {arr}, x = {x}")
    print(f"Output: {result}")
    print(f"Expected: [4, 5, 6, 7]")
    print(f"Pass: {result == [4, 5, 6, 7]}")

    print("\n--- Test Case 2 ---")
    arr = [1, 10, 12, 13, 14]
    x = 2
    result = longest_subarray_diff(arr, x)
    print(f"Input: arr = {arr}, x = {x}")
    print(f"Output: {result}")
    print(f"Expected: [12, 13, 14]")
    print(f"Pass: {result == [12, 13, 14]}")

    print("\n--- Test Case 3 ---")
    arr = [5, 6, 7, 8, 9, 10, 11]
    x = 0
    result = longest_subarray_diff(arr, x)
    print(f"Input: arr = {arr}, x = {x}")
    print(f"Output: {result}")
    print(f"Expected: [5] or single element")
    print(f"Pass: {len(result) == 1}")

    print("\n--- Test Case 4 ---")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 5
    result = longest_subarray_diff(arr, x)
    print(f"Input: arr = {arr}, x = {x}")
    print(f"Output: {result}")
    print(f"Length: {len(result)}")

    print("\n--- Test Case 5 ---")
    arr = []
    x = 3
    result = longest_subarray_diff(arr, x)
    print(f"Input: arr = {arr}, x = {x}")
    print(f"Output: {result}")
    print(f"Expected: []")
    print(f"Pass: {result == []}")


if __name__ == "__main__":
    main()
