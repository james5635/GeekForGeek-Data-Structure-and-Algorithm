from collections import deque


def sliding_window_maximum(arr, k):
    n = len(arr)
    if n == 0 or k == 0:
        return []

    result = []
    dq = deque()

    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


def sliding_window_minimum(arr, k):
    n = len(arr)
    if n == 0 or k == 0:
        return []

    result = []
    dq = deque()

    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


def longest_subarray_bounded_diff(arr, k):
    n = len(arr)
    if n == 0:
        return 0

    max_dq = deque()
    min_dq = deque()
    left = 0
    result = 0

    for right in range(n):
        while max_dq and arr[max_dq[-1]] <= arr[right]:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and arr[min_dq[-1]] >= arr[right]:
            min_dq.pop()
        min_dq.append(right)

        while arr[max_dq[0]] - arr[min_dq[0]] > k:
            left += 1
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()

        result = max(result, right - left + 1)

    return result


if __name__ == "__main__":
    assert sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_maximum([1], 1) == [1]
    assert sliding_window_maximum([9, 11], 2) == [11]

    assert sliding_window_minimum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        -1,
        -3,
        -3,
        -3,
        3,
        3,
    ]
    assert sliding_window_minimum([1], 1) == [1]
    assert sliding_window_minimum([9, 11], 2) == [9]

    assert longest_subarray_bounded_diff([8, 2, 4, 7], 4) == 2
    assert longest_subarray_bounded_diff([10, 1, 2, 4, 7, 2], 5) == 4
    assert longest_subarray_bounded_diff([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3
    print("All tests passed!")
