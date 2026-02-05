"""
Smallest Subarray with K Distinct Elements

Problem: Given an array of integers and a number k, find the smallest subarray
that contains exactly k distinct elements.

Approach: Use sliding window with two pointers and hash map to count frequencies.
Expand window until we have k distinct, then shrink to find minimum.

Time Complexity: O(n) - each element visited at most twice
Space Complexity: O(k) - at most k distinct elements in map
"""

from collections import defaultdict


def smallest_subarray_with_k_distinct(arr, k):
    """
    Find the smallest subarray with exactly k distinct elements.

    Args:
        arr: List of integers
        k: Number of distinct elements required

    Returns:
        Tuple of (start_index, end_index, subarray) or None
    """
    if not arr or k <= 0:
        return None

    n = len(arr)
    freq = defaultdict(int)
    start = 0
    min_length = float("inf")
    result_start = -1
    result_end = -1

    for end in range(n):
        freq[arr[end]] += 1

        # Shrink window while we have more than k distinct
        while len(freq) > k:
            freq[arr[start]] -= 1
            if freq[arr[start]] == 0:
                del freq[arr[start]]
            start += 1

        # Check if current window has exactly k distinct
        if len(freq) == k:
            # Try to shrink further while maintaining k distinct
            temp_start = start
            temp_freq = defaultdict(int)
            temp_freq.update(freq)

            while len(temp_freq) == k:
                current_length = end - temp_start + 1
                if current_length < min_length:
                    min_length = current_length
                    result_start = temp_start
                    result_end = end

                temp_freq[arr[temp_start]] -= 1
                if temp_freq[arr[temp_start]] == 0:
                    del temp_freq[arr[temp_start]]
                temp_start += 1

    if result_start == -1:
        return None

    return (result_start, result_end, arr[result_start : result_end + 1])


def find_all_min_subarrays_with_k_distinct(arr, k):
    """
    Find all subarrays of minimum length with k distinct elements.

    Args:
        arr: List of integers
        k: Number of distinct elements required

    Returns:
        List of subarrays with minimum length
    """
    if not arr or k <= 0:
        return []

    n = len(arr)
    freq = defaultdict(int)
    start = 0
    min_length = float("inf")
    result = []

    for end in range(n):
        freq[arr[end]] += 1

        while len(freq) > k:
            freq[arr[start]] -= 1
            if freq[arr[start]] == 0:
                del freq[arr[start]]
            start += 1

        if len(freq) == k:
            temp_start = start
            temp_freq = defaultdict(int)
            temp_freq.update(freq)

            while len(temp_freq) == k:
                current_length = end - temp_start + 1

                if current_length < min_length:
                    min_length = current_length
                    result = [(temp_start, end, arr[temp_start : end + 1])]
                elif current_length == min_length:
                    result.append((temp_start, end, arr[temp_start : end + 1]))

                temp_freq[arr[temp_start]] -= 1
                if temp_freq[arr[temp_start]] == 0:
                    del temp_freq[arr[temp_start]]
                temp_start += 1

    return result


def length_of_smallest_subarray_k_distinct(arr, k):
    """
    Return just the length of smallest subarray with k distinct elements.

    Args:
        arr: List of integers
        k: Number of distinct elements required

    Returns:
        Length of smallest subarray or -1 if not possible
    """
    result = smallest_subarray_with_k_distinct(arr, k)
    if result is None:
        return -1
    return result[1] - result[0] + 1


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 2, 1, 3, 4, 2, 3]
    k1 = 3
    print(f"Array: {arr1}, k: {k1}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr1, k1)}")
    print()

    # Test Case 2: k equals distinct elements in array
    arr2 = [1, 2, 3, 4, 5]
    k2 = 3
    print(f"Array: {arr2}, k: {k2}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr2, k2)}")
    print()

    # Test Case 3: k = 1
    arr3 = [1, 2, 1, 1, 3]
    k3 = 1
    print(f"Array: {arr3}, k: {k3}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr3, k3)}")
    print()

    # Test Case 4: Not enough distinct elements
    arr4 = [1, 1, 1, 1]
    k4 = 2
    print(f"Array: {arr4}, k: {k4}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr4, k4)}")
    print()

    # Test Case 5: Empty array
    arr5 = []
    k5 = 2
    print(f"Array: {arr5}, k: {k5}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr5, k5)}")
    print()

    # Test Case 6: All elements same
    arr6 = [5, 5, 5, 5, 5]
    k6 = 1
    print(f"Array: {arr6}, k: {k6}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr6, k6)}")
    print()

    # Test Case 7: Negative numbers
    arr7 = [-1, -2, -1, -3, -2]
    k7 = 2
    print(f"Array: {arr7}, k: {k7}")
    print(f"Smallest subarray: {smallest_subarray_with_k_distinct(arr7, k7)}")
    print()

    # Test Case 8: Multiple minimum subarrays
    arr8 = [1, 2, 2, 1, 3, 1, 2]
    k8 = 2
    print(f"Array: {arr8}, k: {k8}")
    print(f"All min subarrays: {find_all_min_subarrays_with_k_distinct(arr8, k8)}")
    print()

    # Test Case 9: Just length
    arr9 = [1, 2, 3, 4, 5]
    k9 = 3
    print(f"Array: {arr9}, k: {k9}")
    print(f"Min length: {length_of_smallest_subarray_k_distinct(arr9, k9)}")
