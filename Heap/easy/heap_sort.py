"""
Heap Sort Algorithm

Problem:
Sort an array using the Heap Sort algorithm based on Binary Heap data structure.

Algorithm:
1. Build a max-heap from the input array (heapify)
2. Repeatedly extract the maximum element:
   - Swap root (max) with last element
   - Reduce heap size by 1
   - Heapify the root
3. Continue until heap size is 1

Heap Sort Algorithm Steps:
1. Convert array into max-heap using heapify (bottom-up)
2. One by one extract elements from heap:
   - Swap arr[0] with arr[n-1]
   - Reduce heap size by 1
   - Call heapify for root

Time Complexity: O(n log n) for all cases
Space Complexity: O(log n) for recursive, O(1) for iterative

Key Properties:
- In-place sorting algorithm
- Not stable (relative order of equal elements may change)
- Typically 2-3x slower than well-implemented QuickSort
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Heapify a subtree rooted at index i.

    Args:
        arr: Array representing the heap
        n: Size of the heap
        i: Root index of the subtree

    After heapify, the subtree rooted at i satisfies max-heap property.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapify_iterative(arr: List[int], n: int, i: int) -> None:
    """
    Iterative version of heapify (avoids recursion).

    Args:
        arr: Array representing the heap
        n: Size of the heap
        i: Root index of the subtree
    """
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heap_sort(arr: List[int], iterative: bool = False) -> List[int]:
    """
    Sort array using Heap Sort algorithm.

    Args:
        arr: Input array to sort
        iterative: If True, use iterative heapify (O(1) space)

    Returns:
        Sorted array (sorted in-place, array is modified)

    Time Complexity: O(n log n) for all cases
    Space Complexity: O(log n) recursive, O(1) iterative
    """
    n = len(arr)

    if n <= 1:
        return arr

    heapify_func = heapify_iterative if iterative else heapify

    for i in range(n // 2 - 1, -1, -1):
        heapify_func(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_func(arr, i, 0)

    return arr


def heap_sort_descending(arr: List[int]) -> List[int]:
    """
    Sort array in descending order using min-heap approach.

    Alternatively, you can use regular heap_sort and reverse the result.
    """
    return sorted(heap_sort(arr.copy()), reverse=True)


class MinHeap:
    """
    Min-Heap implementation for educational purposes.
    Can be used to sort in ascending order more intuitively.
    """

    def __init__(self):
        self.heap = []

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i: int) -> None:
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    def extract_min(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")

        min_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down(0)

        return min_val

    def _sift_down(self, i: int) -> None:
        n = len(self.heap)
        while True:
            smallest = i
            left = self.left_child(i)
            right = self.right_child(i)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def get_min(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)


def heap_sort_using_class(arr: List[int]) -> List[int]:
    """
    Heap sort using the MinHeap class for better understanding.
    """
    min_heap = MinHeap()

    for num in arr:
        min_heap.insert(num)

    result = []
    while min_heap.size() > 0:
        result.append(min_heap.extract_min())

    return result


if __name__ == "__main__":
    test_cases = [
        {"arr": [9, 4, 3, 8, 10, 2, 5], "expected": [2, 3, 4, 5, 8, 9, 10]},
        {"arr": [12, 11, 13, 5, 6, 7], "expected": [5, 6, 7, 11, 12, 13]},
        {"arr": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5]},
        {"arr": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"arr": [1], "expected": [1]},
        {"arr": [], "expected": []},
        {"arr": [3, 3, 3, 1, 1, 2, 2], "expected": [1, 1, 2, 2, 3, 3, 3]},
        {"arr": [-5, -10, -3, -1, -7], "expected": [-10, -7, -5, -3, -1]},
    ]

    print("Heap Sort Test Cases")
    print("=" * 60)

    for i, tc in enumerate(test_cases):
        arr = tc["arr"]
        expected = tc["expected"]

        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        arr_copy3 = arr.copy()

        result_recursive = heap_sort(arr_copy1, iterative=False)
        result_iterative = heap_sort(arr_copy2, iterative=True)
        result_class = heap_sort_using_class(arr_copy3)

        status1 = "PASS" if result_recursive == expected else "FAIL"
        status2 = "PASS" if result_iterative == expected else "FAIL"
        status3 = "PASS" if result_class == expected else "FAIL"

        print(f"\nTest {i + 1}: arr = {arr[:10]}{'...' if len(arr) > 10 else ''}")
        print(f"  Expected: {expected[:10]}{'...' if len(expected) > 10 else ''}")
        print(
            f"  Recursive: {result_recursive[:10]}{'...' if len(result_recursive) > 10 else ''} [{status1}]"
        )
        print(
            f"  Iterative: {result_iterative[:10]}{'...' if len(result_iterative) > 10 else ''} [{status2}]"
        )
        print(
            f"  MinHeap:   {result_class[:10]}{'...' if len(result_class) > 10 else ''} [{status3}]"
        )

    print("\n" + "=" * 60)
    print("\nComplexity Analysis:")
    print("-" * 40)
    print("Time Complexity:  O(n log n) - all cases")
    print("Space Complexity: O(log n) recursive, O(1) iterative")
    print("\nProperties:")
    print("- In-place sorting algorithm")
    print("- Not stable (may change relative order of equal elements)")
    print("- Better than QuickSort for worst-case scenarios")
