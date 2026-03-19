from collections import deque


def maxOfSubarraysNaive(arr, k):
    n = len(arr)
    result = []

    for i in range(n - k + 1):
        max_val = arr[i]
        for j in range(i + 1, i + k):
            max_val = max(max_val, arr[j])
        result.append(max_val)

    return result


import heapq


def maxOfSubarraysHeap(arr, k):
    n = len(arr)
    result = []
    max_heap = []

    for i in range(k):
        heapq.heappush(max_heap, (-arr[i], i))

    result.append(-max_heap[0][0])

    for i in range(k, n):
        heapq.heappush(max_heap, (-arr[i], i))

        while max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)

        result.append(-max_heap[0][0])

    return result


def maxOfSubarrays(arr, k):
    n = len(arr)
    result = []
    dq = deque()

    for i in range(n):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3

    print("Naive approach:", maxOfSubarraysNaive(arr, k))
    print("Heap approach:", maxOfSubarraysHeap(arr, k))
    print("Deque approach:", maxOfSubarrays(arr, k))
