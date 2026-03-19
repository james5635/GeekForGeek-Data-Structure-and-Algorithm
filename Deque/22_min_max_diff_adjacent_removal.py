from collections import deque


def minimize_max_diff(arr, k):
    n = len(arr)
    if k >= n - 1:
        return 0

    diffs = [abs(arr[i + 1] - arr[i]) for i in range(n - 1)]
    result = float("inf")

    dq = deque()
    left = 0
    for right in range(len(diffs)):
        while dq and diffs[dq[-1]] <= diffs[right]:
            dq.pop()
        dq.append(right)

        while dq and dq[0] < left:
            dq.popleft()

        window_size = right - left + 1
        if window_size == n - k - 1:
            result = min(result, diffs[dq[0]])
            left += 1
            while dq and dq[0] < left:
                dq.popleft()

    return result


if __name__ == "__main__":
    assert minimize_max_diff([3, 7, 8, 10, 14], 2) == 2
    assert minimize_max_diff([1, 5, 8, 10], 1) == 3
    assert minimize_max_diff([1, 3, 7, 10, 15], 3) == 2
    assert minimize_max_diff([1, 2, 3, 4, 5], 4) == 0
    assert minimize_max_diff([10, 20], 0) == 10
    print("All tests passed!")
