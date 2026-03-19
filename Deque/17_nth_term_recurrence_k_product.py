from collections import deque


def nth_term_recurrence(arr, n, k):
    if n <= len(arr):
        return arr[n - 1]
    dq = deque(arr)
    for i in range(len(arr), n):
        prod = 1
        for j in range(k):
            prod *= dq[-(j + 1)]
        dq.append(prod)
    return dq[-1]


if __name__ == "__main__":
    arr = [1, 2]
    assert nth_term_recurrence(arr, 5, 2) == 32
    assert nth_term_recurrence([3], 4, 1) == 27
    assert nth_term_recurrence([2, 3], 4, 2) == 216
    assert nth_term_recurrence([1, 2], 1, 2) == 1
    assert nth_term_recurrence([5], 3, 1) == 25
    print("All tests passed!")
