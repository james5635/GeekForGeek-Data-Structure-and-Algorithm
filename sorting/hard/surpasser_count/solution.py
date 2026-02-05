"""
Find Surpasser Count of Each Element in Array

Problem Description:
Given an array arr[] of n integers, the surpasser count of an element
is the number of elements to its right that are greater than it.
Find the surpasser count for each element in the array.

Examples:
- Input: arr[] = [2, 7, 5, 3, 0, 8, 1]
  Output: [4, 1, 1, 1, 2, 0, 0]
  Explanation: For 2, elements to right greater than it: 7,5,3,8 = 4
               For 7, elements to right greater: only 8 = 1
               And so on...

- Input: arr[] = [5, 4, 3, 2, 1]
  Output: [0, 0, 0, 0, 0]

- Input: arr[] = [1, 2, 3, 4, 5]
  Output: [4, 3, 2, 1, 0]

Approach 1: Brute Force
1. For each element, count elements to its right that are greater
2. Time: O(n²), Space: O(1)

Approach 2: Modified Merge Sort (Optimal)
1. Use merge sort to count inversions (reverse of surpasser)
2. While merging, count elements from right subarray that are greater
3. Time: O(n log n), Space: O(n)

Approach 3: Binary Indexed Tree (Fenwick Tree)
1. Coordinate compression + BIT
2. Query count of greater elements to the right
3. Time: O(n log n), Space: O(n)

Time Complexity: O(n log n) using modified merge sort
Space Complexity: O(n)
"""


def find_surpasser_brute_force(arr):
    """
    Find surpasser count using brute force.

    Args:
        arr: Input array

    Returns:
        list: Surpasser count for each element
    """
    if not arr:
        return []

    n = len(arr)
    result = []

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                count += 1
        result.append(count)

    return result


def find_surpasser_merge_sort(arr):
    """
    Find surpasser count using modified merge sort.
    Optimal O(n log n) solution.

    Args:
        arr: Input array

    Returns:
        list: Surpasser count for each element
    """
    if not arr:
        return []

    n = len(arr)

    # Store (value, original_index) pairs
    indexed_arr = [(arr[i], i) for i in range(n)]
    surpasser_count = [0] * n

    def merge_sort(left, right):
        """Modified merge sort to count surpassers."""
        if left >= right:
            return

        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        """Merge two sorted halves and count surpassers."""
        temp = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if indexed_arr[i][0] < indexed_arr[j][0]:
                # Element from left is smaller
                # All remaining elements in right are greater
                temp.append(indexed_arr[i])
                # Count elements in right half that are greater
                surpasser_count[indexed_arr[i][1]] += right - j + 1
                i += 1
            else:
                # Element from right is smaller or equal
                temp.append(indexed_arr[j])
                j += 1

        while i <= mid:
            temp.append(indexed_arr[i])
            i += 1

        while j <= right:
            temp.append(indexed_arr[j])
            j += 1

        # Copy back to original array
        for idx in range(len(temp)):
            indexed_arr[left + idx] = temp[idx]

    merge_sort(0, n - 1)
    return surpasser_count


def find_surpasser_binary_indexed_tree(arr):
    """
    Find surpasser count using Binary Indexed Tree.
    Efficient for large value ranges.

    Args:
        arr: Input array

    Returns:
        list: Surpasser count for each element
    """
    if not arr:
        return []

    n = len(arr)

    # Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
    max_rank = len(sorted_unique)

    # Binary Indexed Tree
    bit = [0] * (max_rank + 2)

    def bit_update(index, delta=1):
        """Update BIT at index."""
        while index <= max_rank:
            bit[index] += delta
            index += index & -index

    def bit_query(index):
        """Query prefix sum up to index."""
        result = 0
        while index > 0:
            result += bit[index]
            index -= index & -index
        return result

    def bit_query_range(left, right):
        """Query range [left, right]."""
        return bit_query(right) - bit_query(left - 1)

    # Process from right to left
    result = [0] * n

    for i in range(n - 1, -1, -1):
        r = rank[arr[i]]
        # Count elements greater than arr[i] (ranks > r)
        result[i] = bit_query_range(r + 1, max_rank)
        bit_update(r)

    return result


def find_surpasser_segment_tree(arr):
    """
    Find surpasser count using Segment Tree.

    Args:
        arr: Input array

    Returns:
        list: Surpasser count for each element
    """
    if not arr:
        return []

    n = len(arr)

    # Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {val: i for i, val in enumerate(sorted_unique)}
    m = len(sorted_unique)

    # Segment tree (4 * m is safe size)
    seg_tree = [0] * (4 * m)

    def seg_update(node, start, end, index):
        """Update segment tree."""
        if start == end:
            seg_tree[node] += 1
            return

        mid = (start + end) // 2
        if index <= mid:
            seg_update(2 * node + 1, start, mid, index)
        else:
            seg_update(2 * node + 2, mid + 1, end, index)

        seg_tree[node] = seg_tree[2 * node + 1] + seg_tree[2 * node + 2]

    def seg_query(node, start, end, left, right):
        """Query range [left, right]."""
        if left > end or right < start:
            return 0

        if left <= start and end <= right:
            return seg_tree[node]

        mid = (start + end) // 2
        return seg_query(2 * node + 1, start, mid, left, right) + seg_query(
            2 * node + 2, mid + 1, end, left, right
        )

    result = [0] * n

    for i in range(n - 1, -1, -1):
        r = rank[arr[i]]
        # Query for elements with rank > r
        if r + 1 < m:
            result[i] = seg_query(0, 0, m - 1, r + 1, m - 1)
        seg_update(0, 0, m - 1, r)

    return result


def find_total_surpassers(arr):
    """
    Calculate total number of surpassers in the array.

    Args:
        arr: Input array

    Returns:
        int: Total surpasser count
    """
    surpassers = find_surpasser_merge_sort(arr)
    return sum(surpassers)


def run_tests():
    """Test cases for surpasser count problem."""
    test_cases = [
        {
            "arr": [2, 7, 5, 3, 0, 8, 1],
            "expected": [4, 1, 1, 1, 2, 0, 0],
            "description": "Standard case",
        },
        {
            "arr": [5, 4, 3, 2, 1],
            "expected": [0, 0, 0, 0, 0],
            "description": "Decreasing array",
        },
        {
            "arr": [1, 2, 3, 4, 5],
            "expected": [4, 3, 2, 1, 0],
            "description": "Increasing array",
        },
        {
            "arr": [1],
            "expected": [0],
            "description": "Single element",
        },
        {
            "arr": [1, 1, 1, 1],
            "expected": [0, 0, 0, 0],
            "description": "All same elements",
        },
        {
            "arr": [3, 1, 4, 1, 5, 9, 2, 6],
            "expected": [4, 5, 3, 4, 2, 0, 1, 0],
            "description": "Mixed values",
        },
        {
            "arr": [],
            "expected": [],
            "description": "Empty array",
        },
        {
            "arr": [10, 5, 3, 8, 12, 1],
            "expected": [1, 2, 2, 1, 0, 0],
            "description": "Unsorted with duplicates",
        },
    ]

    print("Running Surpasser Count Tests:")
    print("=" * 60)

    all_passed = True
    methods = [
        ("Brute Force", find_surpasser_brute_force),
        ("Merge Sort", find_surpasser_merge_sort),
    ]

    for method_name, method in methods:
        print(f"\n--- Testing {method_name} ---")
        for i, test in enumerate(test_cases, 1):
            result = method(test["arr"].copy())
            passed = result == test["expected"]

            status = "PASS" if passed else "FAIL"
            print(f"\nTest {i}: {status}")
            print(f"Description: {test['description']}")
            print(f"Input: {test['arr']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")

            if not passed:
                all_passed = False

    # Test total surpassers
    print("\n--- Testing Total Surpassers ---")
    arr = [2, 7, 5, 3, 0, 8, 1]
    total = find_total_surpassers(arr.copy())
    print(f"Array: {arr}")
    print(f"Total surpassers: {total}")
    print(f"Expected: 9")

    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

    return all_passed


if __name__ == "__main__":
    run_tests()
