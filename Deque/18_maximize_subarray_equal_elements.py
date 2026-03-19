from collections import deque


def maximize_subarray(A, K):
    n = len(A)
    if n == 0:
        return 0
    left = 0
    total = 0
    dq = deque()
    result = 0
    for right in range(n):
        while dq and A[dq[-1]] < A[right]:
            dq.pop()
        dq.append(right)
        total += A[right]
        while dq and A[dq[0]] * (right - left + 1) - total > K:
            total -= A[left]
            if dq and dq[0] == left:
                dq.popleft()
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    assert maximize_subarray([2, 4, 8, 5, 9, 6], 6) == 3
    assert maximize_subarray([3, 3, 3], 0) == 3
    assert maximize_subarray([1, 5, 1], 3) == 3
    assert maximize_subarray([1], 10) == 1
    assert maximize_subarray([], 5) == 0
    print("All tests passed!")
