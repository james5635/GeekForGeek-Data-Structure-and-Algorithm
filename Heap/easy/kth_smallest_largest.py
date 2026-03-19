"""
K'th Smallest (and K'th Largest) Element in an Unsorted Array

Problem:
Given an integer array arr[] and an integer k, find the k'th smallest element.

Examples:
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5 (4th smallest element)

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7 (3rd smallest element)

Approaches:
1. Sorting - O(n log n) time, O(1) space
2. Max-Heap - O(n log k) time, O(k) space
3. QuickSelect - O(n) average, O(n^2) worst, O(n) space
4. Counting Sort - O(n + max) time, O(max) space

Time Complexity Analysis:
- Sorting: O(n log n) - simple but not optimal for small k
- Max-Heap: O(n log k) - efficient when k << n
- QuickSelect: O(n) average case
- Counting Sort: O(n + maxElement)

Space Complexity:
- Sorting: O(1)
- Max-Heap: O(k)
- QuickSelect: O(1) or O(n) for recursion stack
- Counting Sort: O(maxElement)
"""

from typing import List
import heapq


def kth_smallest_sorting(arr: List[int], k: int) -> int:
    """
    Find k'th smallest element using sorting.

    Approach:
    1. Sort the array
    2. Return element at index k-1

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    arr_sorted = sorted(arr)
    return arr_sorted[k - 1]


def kth_smallest_max_heap(arr: List[int], k: int) -> int:
    """
    Find k'th smallest element using max-heap.

    Approach:
    1. Maintain a max-heap of size k
    2. For each element, push to heap
    3. If heap size exceeds k, pop the largest
    4. The heap always contains k smallest elements
    5. Top of heap is k'th smallest

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    pq = []

    for num in arr:
        heapq.heappush(pq, -num)
        if len(pq) > k:
            heapq.heappop(pq)

    return -pq[0]


def kth_smallest_quickselect(arr: List[int], k: int) -> int:
    """
    Find k'th smallest element using QuickSelect algorithm.

    Approach:
    1. Partition array around a pivot
    2. If pivot is at index k-1, return it
    3. If pivot index > k-1, search left side
    4. Otherwise, search right side

    Time Complexity: O(n) average, O(n^2) worst
    Space Complexity: O(1) or O(n) for recursion
    """

    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        store_idx = left

        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1

        arr[right], arr[store_idx] = arr[store_idx], arr[right]
        return store_idx

    def quick_select(left: int, right: int, k_idx: int) -> int:
        if left == right:
            return arr[left]

        pivot_idx = right
        pivot_new_idx = partition(left, right, pivot_idx)

        if pivot_new_idx == k_idx:
            return arr[pivot_new_idx]
        elif pivot_new_idx > k_idx:
            return quick_select(left, pivot_new_idx - 1, k_idx)
        else:
            return quick_select(pivot_new_idx + 1, right, k_idx)

    return quick_select(0, len(arr) - 1, k - 1)


def kth_smallest_counting_sort(arr: List[int], k: int) -> int:
    """
    Find k'th smallest element using counting sort approach.

    Approach:
    1. Find maximum element
    2. Create frequency array
    3. Calculate cumulative frequency
    4. Find element where cumulative >= k

    Note: Only efficient when range of elements is small

    Time Complexity: O(n + maxElement)
    Space Complexity: O(maxElement)
    """
    max_element = max(arr)
    freq = [0] * (max_element + 1)

    for num in arr:
        freq[num] += 1

    count = 0
    for i in range(max_element + 1):
        if freq[i] != 0:
            count += freq[i]
            if count >= k:
                return i

    return -1


def kth_largest_sorting(arr: List[int], k: int) -> int:
    """
    Find k'th largest element using sorting.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[k - 1]


def kth_largest_min_heap(arr: List[int], k: int) -> int:
    """
    Find k'th largest element using min-heap.

    Approach:
    1. Maintain a min-heap of size k
    2. The heap always contains k largest elements
    3. Top of heap is k'th largest

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k > len(arr):
        return -1

    pq = arr[:k]
    heapq.heapify(pq)

    for i in range(k, len(arr)):
        if arr[i] > pq[0]:
            heapq.heapreplace(pq, arr[i])

    return pq[0]


def kth_smallest(arr: List[int], k: int, method: str = "heap") -> int:
    """
    Find k'th smallest element using specified method.

    Args:
        arr: Input array
        k: Position (1-indexed)
        method: "sorting", "heap", "quickselect", or "counting"

    Returns:
        k'th smallest element

    Time Complexity:
        - sorting: O(n log n)
        - heap: O(n log k)
        - quickselect: O(n) average
        - counting: O(n + max)

    Space Complexity:
        - sorting: O(1)
        - heap: O(k)
        - quickselect: O(1) amortized
        - counting: O(max)
    """
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")

    if method == "sorting":
        return kth_smallest_sorting(arr, k)
    elif method == "heap":
        return kth_smallest_max_heap(arr, k)
    elif method == "quickselect":
        return kth_smallest_quickselect(arr.copy(), k)
    elif method == "counting":
        return kth_smallest_counting_sort(arr, k)
    else:
        raise ValueError(f"Unknown method: {method}")


if __name__ == "__main__":
    test_cases = [
        {"arr": [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], "k": 4, "expected_smallest": 5},
        {"arr": [7, 10, 4, 3, 20, 15], "k": 3, "expected_smallest": 7},
        {"arr": [12, 3, 5, 7, 19], "k": 2, "expected_smallest": 5},
        {"arr": [1, 2, 3, 4, 5], "k": 1, "expected_smallest": 1},
        {"arr": [5, 4, 3, 2, 1], "k": 5, "expected_smallest": 5},
    ]

    print("K'th Smallest Element Test Cases")
    print("=" * 60)

    methods = ["sorting", "heap", "quickselect", "counting"]

    for i, tc in enumerate(test_cases):
        arr = tc["arr"]
        k = tc["k"]
        expected = tc["expected_smallest"]

        print(f"\nTest {i + 1}: arr = {arr}, k = {k}")
        print(f"  Expected k'th smallest: {expected}")

        for method in methods:
            try:
                result = kth_smallest(arr.copy(), k, method)
                status = "PASS" if result == expected else "FAIL"
                print(f"  {method:12s}: {result:5} [{status}]")
            except Exception as e:
                print(f"  {method:12s}: Error - {e}")

    print("\n" + "=" * 60)
    print("\nK'th Largest Element Test Cases")
    print("=" * 60)

    for i, tc in enumerate(test_cases):
        arr = tc["arr"]
        k = tc["k"]
        n = len(arr)
        expected_largest = sorted(arr, reverse=True)[k - 1]

        print(f"\nTest {i + 1}: arr = {arr}, k = {k}")
        print(f"  Expected k'th largest: {expected_largest}")

        result = kth_largest_sorting(arr, k)
        print(f"  sorting: {result}")

        result = kth_largest_min_heap(arr, k)
        print(f"  min_heap: {result}")
