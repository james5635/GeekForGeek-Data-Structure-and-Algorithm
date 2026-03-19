from collections import deque


def longest_subarray_max_diff(arr, x):
    if not arr:
        return []

    min_dq = deque()
    max_dq = deque()
    left = 0
    best_len = 0
    best_start = 0

    for right in range(len(arr)):
        while min_dq and arr[min_dq[-1]] >= arr[right]:
            min_dq.pop()
        min_dq.append(right)

        while max_dq and arr[max_dq[-1]] <= arr[right]:
            max_dq.pop()
        max_dq.append(right)

        while arr[max_dq[0]] - arr[min_dq[0]] > x:
            if min_dq[0] == left:
                min_dq.popleft()
            if max_dq[0] == left:
                max_dq.popleft()
            left += 1

        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_start = left

    return arr[best_start : best_start + best_len]


if __name__ == "__main__":
    print(longest_subarray_max_diff([8, 4, 5, 6, 7], 3))
    print(longest_subarray_max_diff([1, 10, 20, 30, 40], 5))
    print(longest_subarray_max_diff([1, 2, 3, 4, 5], 1))
    print(longest_subarray_max_diff([5, 5, 5, 5], 0))
    print(longest_subarray_max_diff([1], 0))
    print(longest_subarray_max_diff([10, 1, 2, 4, 7, 2], 5))
