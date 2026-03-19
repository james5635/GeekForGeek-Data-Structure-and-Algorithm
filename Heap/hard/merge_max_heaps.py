"""
Merge Two Binary Max Heaps
URL: https://www.geeksforgeeks.org/merge-two-binary-max-heaps/
Source: GeeksforGeeks

Problem:
Given two binary max heaps, merge them to form a new max heap.

Examples:
Input: a[] = {10, 5, 6, 2}, b[] = {12, 7, 9}
Output: {12, 10, 9, 2, 5, 7, 6}

Input: a[] = {2, 5, 1, 9, 12}, b[] = {3, 7, 4, 10}
Output: {12, 10, 7, 9, 5, 3, 1, 4, 2}

Approaches:
1. Naive: Insert elements into new max heap - O((N+M)*log(N+M))
2. Efficient: Merge arrays and build max heap - O(N+M)

A binary max heap is a complete binary tree where each node is greater
than or equal to its children. In array representation:
- Parent at index i
- Left child at 2*i + 1
- Right child at 2*i + 2
"""

import heapq


def max_heapify(arr, n, idx):
    """
    Standard heapify function to heapify a subtree rooted at idx.
    Assumes subtrees are already heapified.

    Args:
        arr: Array representing the heap
        n: Size of the heap
        idx: Index of the root of subtree to heapify
    """
    if idx >= n:
        return

    left = 2 * idx + 1
    right = 2 * idx + 2
    largest = idx

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Build a max heap from an unsorted array.

    Args:
        arr: Unsorted array

    Time: O(n)
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def merge_heaps_naive(a, b):
    """
    Naive approach: Insert elements into max heap one by one.

    Algorithm:
    1. Create max heap (by negating values since Python has min-heap)
    2. Insert all elements from both arrays
    3. Extract all elements

    Time: O((N+M) * log(N+M))
    Space: O(N+M)

    Args:
        a: First max heap array
        b: Second max heap array

    Returns:
        Merged max heap array
    """
    max_heap = []

    for num in a:
        heapq.heappush(max_heap, -num)

    for num in b:
        heapq.heappush(max_heap, -num)

    merged = []
    while max_heap:
        merged.append(-heapq.heappop(max_heap))

    return merged


def merge_heaps(a, b):
    """
    Efficient approach: Merge and build heap.

    Algorithm:
    1. Concatenate both arrays
    2. Build max heap from combined array

    Time: O(N + M)
    Space: O(N + M)

    Args:
        a: First max heap array
        b: Second max heap array

    Returns:
        Merged max heap array
    """
    merged = a + b
    build_max_heap(merged)
    return merged


def merge_heaps_inplace(a, b):
    """
    Merge heaps and modify in place.
    """
    a.extend(b)
    build_max_heap(a)
    return a


def merge_heaps_custom_heap(a, b):
    """
    Using custom max heap class implementation.
    """

    class MaxHeap:
        def __init__(self):
            self.heap = []

        def parent(self, i):
            return (i - 1) // 2

        def left(self, i):
            return 2 * i + 1

        def right(self, i):
            return 2 * i + 2

        def insert(self, key):
            self.heap.append(key)
            self._heapify_up(len(self.heap) - 1)

        def _heapify_up(self, i):
            while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
                self.heap[i], self.heap[self.parent(i)] = (
                    self.heap[self.parent(i)],
                    self.heap[i],
                )
                i = self.parent(i)

        def get_max(self):
            if not self.heap:
                return None
            return self.heap[0]

        def extract_max(self):
            if not self.heap:
                return None

            max_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()

            if self.heap:
                self._heapify_down(0)

            return max_val

        def _heapify_down(self, i):
            while True:
                largest = i
                left = self.left(i)
                right = self.right(i)

                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = left

                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = right

                if largest != i:
                    self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                    i = largest
                else:
                    break

        def __len__(self):
            return len(self.heap)

    heap = MaxHeap()

    for num in a:
        heap.insert(num)

    for num in b:
        heap.insert(num)

    result = []
    while len(heap) > 0:
        result.append(heap.extract_max())

    return result


def is_max_heap(arr):
    """
    Check if array represents a valid max heap.
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            return False

        if right < n and arr[i] < arr[right]:
            return False

    return True


def visualize_heap(arr):
    """
    Simple visualization of heap structure.
    """
    if not arr:
        return "Empty heap"

    lines = []
    level = 0
    i = 0
    level_nodes = 1

    while i < len(arr):
        level_nodes = min(2**level, len(arr) - i)
        level_str = ""

        for j in range(level_nodes):
            level_str += str(arr[i]) + " "
            i += 1

        lines.append("  " * (3 - level) + level_str)
        level += 1

    return "\n".join(lines)


if __name__ == "__main__":
    print("=" * 60)
    print("MERGE TWO BINARY MAX HEAPS")
    print("=" * 60)

    test_cases = [
        {"a": [10, 5, 6, 2], "b": [12, 7, 9], "expected": [12, 10, 9, 2, 5, 7, 6]},
        {
            "a": [2, 5, 1, 9, 12],
            "b": [3, 7, 4, 10],
            "expected": [12, 10, 7, 9, 5, 3, 1, 4, 2],
        },
        {"a": [1], "b": [2], "expected": [2, 1]},
        {"a": [5, 3, 2], "b": [8, 6, 4], "expected": [8, 6, 4, 3, 5, 2]},
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"TEST CASE {i}")
        print("=" * 60)

        a = test["a"]
        b = test["b"]
        expected = test["expected"]

        print(f"\nInput:")
        print(f"  Heap A: {a}")
        print(f"  Heap B: {b}")

        print(f"\nHeap A structure:")
        print(visualize_heap(a))
        print(f"\nHeap B structure:")
        print(visualize_heap(b))

        result_naive = merge_heaps_naive(a[:], b[:])
        result_efficient = merge_heaps(a[:], b[:])
        result_custom = merge_heaps_custom_heap(a[:], b[:])

        print(f"\nExpected output:    {expected}")
        print(f"Naive (using heap): {result_naive}")
        print(f"Efficient (build):  {result_efficient}")
        print(f"Custom class:       {result_custom}")

        print(f"\nValid max heap check:")
        print(f"  Naive result:     {is_max_heap(result_naive)}")
        print(f"  Efficient result: {is_max_heap(result_efficient)}")

        status = "PASS" if result_efficient == expected else "FAIL"
        print(f"\n  Status: {status}")

        if status == "PASS":
            print(f"\nMerged heap structure:")
            print(visualize_heap(result_efficient))

    print("\n" + "=" * 60)
    print("APPROACH COMPARISON")
    print("=" * 60)

    import time

    large_a = list(range(1000, 0, -1))
    large_b = list(range(2000, 1000, -1))

    print(f"\nLarge test (1000 + 1000 elements):")

    start = time.time()
    result1 = merge_heaps_naive(large_a[:], large_b[:])
    naive_time = time.time() - start

    start = time.time()
    result2 = merge_heaps(large_a[:], large_b[:])
    efficient_time = time.time() - start

    print(f"  Naive approach:     {naive_time:.6f} seconds")
    print(f"  Efficient approach: {efficient_time:.6f} seconds")
    print(f"  Speedup:            {naive_time / efficient_time:.2f}x")

    print("\n" + "=" * 60)
    print("ALGORITHM EXPLANATION")
    print("=" * 60)
    print("""
Efficient Approach (Merge + Build Heap):
-----------------------------------------
1. Concatenate both arrays: merged = a + b
2. Build max heap from merged array

Why this is efficient:
- Merging arrays: O(N + M)
- Building heap: O(N + M)
- Total: O(N + M)

Build Max Heap Process:
- Start from last non-leaf node: index (n//2 - 1)
- Heapify each node going upward
- Each heapify: O(log n)
- Total: O(n)

Naive Approach (Element by Element):
-------------------------------------
1. Create empty max heap
2. Insert all elements from both arrays: O((N+M) * log(N+M))
3. Extract all elements: O((N+M) * log(N+M))
4. Total: O((N+M) * log(N+M))

Max Heap Properties:
--------------------
- Complete binary tree (filled left to right)
- Parent >= Children
- Array representation:
  - Parent(i) = (i-1) // 2
  - Left(i) = 2*i + 1
  - Right(i) = 2*i + 2
""")

    print("=" * 60)
    print("COMPLEXITY ANALYSIS")
    print("=" * 60)
    print("\n1. Naive (Insert Elements One by One):")
    print("   Time:  O((N+M) * log(N+M))")
    print("   Space: O(N+M)")
    print("\n2. Efficient (Merge + Build Heap):")
    print("   Time:  O(N + M)")
    print("   Space: O(N + M)")
    print("\nWhere N = size of first heap, M = size of second heap")
