"""
Kth Distinct Element in Array

Problem: Given an array of integers and a number k, find the kth distinct element
in the array. Distinct elements are those that appear exactly once in the array.

Approach: Use hash map to count frequencies, then find elements with frequency 1,
and return the kth such element in order of first appearance.

Time Complexity: O(n) - single pass to count, single pass to find kth
Space Complexity: O(n) - hash map for frequencies
"""

from collections import OrderedDict


def kth_distinct_element(arr, k):
    """
    Find the kth distinct element (appears exactly once).

    Args:
        arr: List of integers
        k: Position of distinct element to find (1-based)

    Returns:
        kth distinct element or None if not enough distinct elements
    """
    if not arr or k <= 0:
        return None

    # Count frequencies
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find kth element with frequency 1
    count = 0
    for num in arr:
        if freq[num] == 1:
            count += 1
            if count == k:
                return num

    return None


def kth_distinct_element_ordered(arr, k):
    """
    Find kth distinct element using OrderedDict to maintain order.

    Args:
        arr: List of integers
        k: Position of distinct element to find

    Returns:
        kth distinct element or None
    """
    if not arr or k <= 0:
        return None

    freq = OrderedDict()
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    count = 0
    for num, frequency in freq.items():
        if frequency == 1:
            count += 1
            if count == k:
                return num

    return None


def get_all_distinct_elements(arr):
    """
    Get all distinct elements in order of first appearance.

    Args:
        arr: List of integers

    Returns:
        List of distinct elements
    """
    if not arr:
        return []

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    distinct = []
    seen = set()
    for num in arr:
        if freq[num] == 1 and num not in seen:
            distinct.append(num)
            seen.add(num)

    return distinct


def count_distinct_elements(arr):
    """
    Count total number of distinct elements.

    Args:
        arr: List of integers

    Returns:
        Count of distinct elements
    """
    if not arr:
        return 0

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return sum(1 for count in freq.values() if count == 1)


def first_k_distinct_elements(arr, k):
    """
    Get first k distinct elements.

    Args:
        arr: List of integers
        k: Number of distinct elements to get

    Returns:
        List of first k distinct elements
    """
    all_distinct = get_all_distinct_elements(arr)
    return all_distinct[:k]


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 2, 1, 3, 4, 2, 5]
    k1 = 2
    print(f"Array: {arr1}, k: {k1}")
    print(f"Kth distinct element: {kth_distinct_element(arr1, k1)}")
    print(f"All distinct: {get_all_distinct_elements(arr1)}")
    print()

    # Test Case 2: k = 1 (first distinct)
    arr2 = [1, 2, 2, 3, 3, 4]
    k2 = 1
    print(f"Array: {arr2}, k: {k2}")
    print(f"Kth distinct element: {kth_distinct_element(arr2, k2)}")
    print()

    # Test Case 3: k larger than distinct count
    arr3 = [1, 1, 1, 1]
    k3 = 2
    print(f"Array: {arr3}, k: {k3}")
    print(f"Kth distinct element: {kth_distinct_element(arr3, k3)}")
    print(f"Count of distinct: {count_distinct_elements(arr3)}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    k4 = 1
    print(f"Array: {arr4}, k: {k4}")
    print(f"Kth distinct element: {kth_distinct_element(arr4, k4)}")
    print()

    # Test Case 5: All distinct
    arr5 = [1, 2, 3, 4, 5]
    k5 = 3
    print(f"Array: {arr5}, k: {k5}")
    print(f"Kth distinct element: {kth_distinct_element(arr5, k5)}")
    print(f"First {k5} distinct: {first_k_distinct_elements(arr5, k5)}")
    print()

    # Test Case 6: Negative numbers
    arr6 = [-1, -2, -1, -3, -2, -4]
    k6 = 2
    print(f"Array: {arr6}, k: {k6}")
    print(f"Kth distinct element: {kth_distinct_element(arr6, k6)}")
    print()

    # Test Case 7: k = last distinct
    arr7 = [1, 2, 1, 3, 2, 4, 5, 5]
    k7 = 3
    print(f"Array: {arr7}, k: {k7}")
    print(f"Kth distinct element: {kth_distinct_element(arr7, k7)}")
    print(f"All distinct: {get_all_distinct_elements(arr7)}")
    print()

    # Test Case 8: Large k
    arr8 = [1, 2, 3, 4, 5, 6, 7, 8]
    k8 = 10
    print(f"Array: {arr8}, k: {k8}")
    print(f"Kth distinct element: {kth_distinct_element(arr8, k8)}")
    print()

    # Test Case 9: Invalid k
    arr9 = [1, 2, 3]
    k9 = 0
    print(f"Array: {arr9}, k: {k9}")
    print(f"Kth distinct element: {kth_distinct_element(arr9, k9)}")
