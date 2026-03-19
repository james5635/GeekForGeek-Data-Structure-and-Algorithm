from collections import deque


def sliding_window_maximum_naive(arr, k):
    n = len(arr)
    result = []
    for i in range(n - k + 1):
        max_val = arr[i]
        for j in range(1, k):
            max_val = max(max_val, arr[i + j])
        result.append(max_val)
    return result


def sliding_window_maximum_deque(arr, k):
    n = len(arr)
    dq = deque()
    result = []

    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


if __name__ == "__main__":
    arr = [1, 3, 2, 1, 7, 3]
    k = 3
    print(sliding_window_maximum_naive(arr, k))
    print(sliding_window_maximum_deque(arr, k))
