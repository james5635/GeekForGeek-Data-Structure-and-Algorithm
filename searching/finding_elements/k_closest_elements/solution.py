"""
K Closest Elements

Problem:
Given a sorted array arr[], two integers k and x, find the k closest
elements to x in the array. Result should be sorted in ascending order.

Examples:
Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
Output: [1, 2, 3, 4]

Input: arr = [1, 2, 3, 4, 5], k = 4, x = -1
Output: [1, 2, 3, 4]

Approach:
Binary Search + Two Pointers - First use binary search to find the
position of x or closest element, then expand outward using two pointers
to find k closest elements.

Alternative: Binary search for the left bound directly.

Time Complexity: O(log n + k)
Space Complexity: O(1) auxiliary, O(k) for result

Reference:
https://www.geeksforgeeks.org/dsa/k-closest-elements/
"""

import bisect


def find_k_closest_elements(arr, k, x):
    """
    Find k closest elements to x in sorted array.

    Args:
        arr: Sorted list of integers
        k: Number of closest elements to find
        x: Target value

    Returns:
        List of k closest elements in ascending order
    """
    n = len(arr)

    if k >= n:
        return arr

    # Binary search for insertion point of x
    idx = bisect.bisect_left(arr, x)

    # Two pointers to expand from position near x
    left = idx - 1
    right = idx

    # Result list
    result = []

    # Collect k closest elements
    while len(result) < k:
        # Check bounds and compare distances
        if left >= 0 and right < n:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        elif left >= 0:
            result.append(arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1

    # Sort result since we collected in arbitrary order
    return sorted(result)


def find_k_closest_optimized(arr, k, x):
    """
    Optimized version using binary search for left bound.
    Time: O(log(n-k) + k)
    """
    n = len(arr)

    if k >= n:
        return arr

    # Binary search for the leftmost index of k elements
    left, right = 0, n - k

    while left < right:
        mid = left + (right - left) // 2

        # Compare distance of mid vs mid+k to x
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left : left + k]


def test_k_closest():
    """Test cases for k closest elements."""
    # Test case 1: Basic
    assert find_k_closest_elements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

    # Test case 2: x less than all elements
    assert find_k_closest_elements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]

    # Test case 3: x greater than all elements
    assert find_k_closest_elements([1, 2, 3, 4, 5], 4, 10) == [2, 3, 4, 5]

    # Test case 4: With duplicates
    assert find_k_closest_elements([1, 1, 2, 2, 3, 3], 3, 2) == [1, 2, 2]

    # Test case 5: k = 1
    assert find_k_closest_elements([1, 2, 3, 4, 5], 1, 3) == [3]

    # Test case 6: Even distance - prefer smaller
    assert find_k_closest_elements([1, 2, 3, 5, 6], 2, 4) == [3, 5]

    # Test optimized version
    assert find_k_closest_optimized([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(f"Array: {arr}")
    print(f"k = {k}, x = {x}")
    print(f"K closest elements: {find_k_closest_elements(arr, k, x)}")
    print(f"K closest (optimized): {find_k_closest_optimized(arr, k, x)}")

    # Run tests
    test_k_closest()
