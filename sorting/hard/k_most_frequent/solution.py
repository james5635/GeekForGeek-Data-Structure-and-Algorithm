"""
Find K Numbers with Most Occurrences

Problem Description:
Given an array of n numbers and a positive integer k, find the k numbers
that appear the most frequently in the array. The numbers should be printed
in decreasing order of their frequencies. If two numbers have same frequency,
the larger number should be given preference.

Examples:
- Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
  Output: [4, 1]
  Explanation: Frequency of 4 = 2, Frequency of 1 = 2
               Since 4 > 1, 4 is printed first

- Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
  Output: [5, 11, 7, 10]

Approach 1: Hash Map + Sorting
1. Count frequency of each element using hash map - O(n)
2. Sort elements by frequency (descending), then by value (descending) - O(n log n)
3. Return first k elements - O(k)

Approach 2: Hash Map + Min Heap (Optimal for large n)
1. Count frequency of each element - O(n)
2. Use min heap of size k to keep track of top k frequent elements
3. Return elements from heap - O(k)

Approach 3: Hash Map + Bucket Sort
1. Count frequency of each element - O(n)
2. Create buckets where index = frequency - O(n)
3. Collect elements from highest frequency bucket - O(n)

Time Complexity: O(n log k) using heap approach
Space Complexity: O(n) for storing frequencies
"""

from collections import Counter
import heapq


def k_most_frequent_sorting(arr, k):
    """
    Find k most frequent elements using sorting.

    Args:
        arr: Input array
        k: Number of top frequent elements to find

    Returns:
        list: k most frequent elements in decreasing order of frequency
    """
    if not arr or k <= 0:
        return []

    # Count frequencies
    freq = Counter(arr)

    # Sort by frequency (descending), then by value (descending)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))

    # Return top k elements
    return [item[0] for item in sorted_items[:k]]


def k_most_frequent_heap(arr, k):
    """
    Find k most frequent elements using min heap.
    More efficient for large arrays.

    Args:
        arr: Input array
        k: Number of top frequent elements to find

    Returns:
        list: k most frequent elements in decreasing order of frequency
    """
    if not arr or k <= 0:
        return []

    # Count frequencies
    freq = Counter(arr)

    # Use min heap to keep track of top k elements
    # Store (frequency, -value) to handle tie-breaking (larger value first)
    min_heap = []

    for num, count in freq.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (count, -num))
        elif count > min_heap[0][0] or (
            count == min_heap[0][0] and num > -min_heap[0][1]
        ):
            heapq.heapreplace(min_heap, (count, -num))

    # Extract elements and sort properly
    result = [(-num, count) for count, num in min_heap]
    # Sort by frequency descending, then by value descending
    result.sort(key=lambda x: (-x[1], -x[0]))

    return [num for num, count in result]


def k_most_frequent_bucket_sort(arr, k):
    """
    Find k most frequent elements using bucket sort.
    Efficient when frequency range is limited.

    Args:
        arr: Input array
        k: Number of top frequent elements to find

    Returns:
        list: k most frequent elements in decreasing order of frequency
    """
    if not arr or k <= 0:
        return []

    # Count frequencies
    freq = Counter(arr)

    # Find max frequency
    max_freq = max(freq.values()) if freq else 0

    # Create buckets
    buckets = [[] for _ in range(max_freq + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    # Collect from highest frequency buckets
    result = []
    for i in range(max_freq, 0, -1):
        # Sort elements in bucket by value (descending) for tie-breaking
        buckets[i].sort(reverse=True)
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result


def k_most_frequent_quickselect(arr, k):
    """
    Find k most frequent elements using quickselect-like approach.

    Args:
        arr: Input array
        k: Number of top frequent elements to find

    Returns:
        list: k most frequent elements in decreasing order of frequency
    """
    if not arr or k <= 0:
        return []

    # Count frequencies
    freq = Counter(arr)
    items = list(freq.items())

    def partition(left, right, pivot_idx):
        pivot_freq = items[pivot_idx][1]
        pivot_val = items[pivot_idx][0]

        # Move pivot to end
        items[pivot_idx], items[right] = items[right], items[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if items[i][1] > pivot_freq or (
                items[i][1] == pivot_freq and items[i][0] > pivot_val
            ):
                items[store_idx], items[i] = items[i], items[store_idx]
                store_idx += 1

        items[right], items[store_idx] = items[store_idx], items[right]
        return store_idx

    def quickselect(left, right, k_smallest):
        if left == right:
            return

        pivot_idx = (left + right) // 2
        pivot_idx = partition(left, right, pivot_idx)

        if k_smallest == pivot_idx:
            return
        elif k_smallest < pivot_idx:
            quickselect(left, pivot_idx - 1, k_smallest)
        else:
            quickselect(pivot_idx + 1, right, k_smallest)

    quickselect(0, len(items) - 1, k - 1)

    # Get top k and sort them
    top_k = items[:k]
    top_k.sort(key=lambda x: (-x[1], -x[0]))

    return [item[0] for item in top_k]


def run_tests():
    """Test cases for k most frequent elements problem."""
    test_cases = [
        {
            "arr": [3, 1, 4, 4, 5, 2, 6, 1],
            "k": 2,
            "expected": [4, 1],
            "description": "Standard case with tie-breaking",
        },
        {
            "arr": [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9],
            "k": 4,
            "expected": [5, 11, 7, 10],
            "description": "Four most frequent",
        },
        {
            "arr": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
            "description": "Different frequencies",
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "k": 3,
            "expected": [5, 4, 3],
            "description": "All unique elements",
        },
        {
            "arr": [1, 1, 1, 1, 1],
            "k": 1,
            "expected": [1],
            "description": "Single element repeated",
        },
        {
            "arr": [],
            "k": 2,
            "expected": [],
            "description": "Empty array",
        },
        {
            "arr": [5, 3, 1, 5, 3, 1],
            "k": 3,
            "expected": [5, 3, 1],
            "description": "All same frequency",
        },
        {
            "arr": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
            "k": 2,
            "expected": [4, 3],
            "description": "Decreasing frequency order",
        },
        {
            "arr": [100, 100, 50, 50, 25, 25, 25],
            "k": 2,
            "expected": [25, 100],
            "description": "Larger values with same frequency",
        },
    ]

    print("Running K Most Frequent Elements Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Sorting", k_most_frequent_sorting),
        ("Bucket Sort", k_most_frequent_bucket_sort),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy(), test["k"])
            passed = result == test["expected"]

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input: {test['arr']}, k={test['k']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")

            if not passed:
                all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()
