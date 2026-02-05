"""
Frequent Element in Array

Problem: Given an array, find the most frequent element(s) in the array.
If multiple elements have the same maximum frequency, return any or all of them.

Example:
    Input: arr[] = {1, 3, 2, 1, 4, 1}
    Output: 1 (frequency = 3)

    Input: arr[] = {10, 20, 10, 20, 30, 20, 20}
    Output: 20 (frequency = 4)

Approach:
    Use a hash map (dictionary) to count frequencies of all elements,
    then find the element(s) with maximum frequency.

Time Complexity: O(n) where n is the size of the array
Space Complexity: O(n) for storing frequency counts
"""


def most_frequent(arr):
    """
    Find the most frequent element in the array.
    Returns the first encountered element if there are ties.

    Args:
        arr: List of integers

    Returns:
        int: Most frequent element, or None if array is empty
    """
    if not arr:
        return None

    frequency = {}
    max_count = 0
    most_freq_element = arr[0]

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > max_count:
            max_count = frequency[num]
            most_freq_element = num

    return most_freq_element


def most_frequent_all(arr):
    """
    Find all elements that have the maximum frequency.

    Args:
        arr: List of integers

    Returns:
        list: List of most frequent elements
    """
    if not arr:
        return []

    from collections import Counter

    frequency = Counter(arr)
    max_count = max(frequency.values())

    return [num for num, count in frequency.items() if count == max_count]


def most_frequent_with_count(arr):
    """
    Find the most frequent element along with its frequency.

    Args:
        arr: List of integers

    Returns:
        tuple: (most_frequent_element, frequency)
    """
    if not arr:
        return None, 0

    from collections import Counter

    frequency = Counter(arr)
    most_common = frequency.most_common(1)[0]

    return most_common


def top_k_frequent(arr, k):
    """
    Find the top k most frequent elements.

    Args:
        arr: List of integers
        k: Number of top frequent elements to return

    Returns:
        list: List of tuples (element, frequency)
    """
    if not arr or k <= 0:
        return []

    from collections import Counter

    frequency = Counter(arr)
    return frequency.most_common(k)


def least_frequent(arr):
    """
    Find the least frequent element(s) in the array.

    Args:
        arr: List of integers

    Returns:
        list: List of least frequent elements
    """
    if not arr:
        return []

    from collections import Counter

    frequency = Counter(arr)
    min_count = min(frequency.values())

    return [num for num, count in frequency.items() if count == min_count]


def frequency_distribution(arr):
    """
    Get the complete frequency distribution of the array.

    Args:
        arr: List of integers

    Returns:
        dict: Dictionary with elements as keys and frequencies as values
    """
    from collections import Counter

    return dict(Counter(arr))


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr = [1, 3, 2, 1, 4, 1]
    print(f"Test 1 - Most frequent: {most_frequent(arr)}")  # Expected: 1

    # Test Case 2: Another standard case
    arr = [10, 20, 10, 20, 30, 20, 20]
    print(f"Test 2 - Most frequent: {most_frequent(arr)}")  # Expected: 20

    # Test Case 3: Tie for most frequent
    arr = [1, 2, 3, 1, 2, 3]
    print(
        f"Test 3 - Most frequent (first): {most_frequent(arr)}"
    )  # Expected: 1 or 2 or 3
    print(
        f"Test 3 - All most frequent: {sorted(most_frequent_all(arr))}"
    )  # Expected: [1, 2, 3]

    # Test Case 4: All unique elements
    arr = [1, 2, 3, 4, 5]
    print(f"Test 4 - Most frequent: {most_frequent(arr)}")  # Expected: 1
    print(
        f"Test 4 - All most frequent: {sorted(most_frequent_all(arr))}"
    )  # Expected: [1, 2, 3, 4, 5]

    # Test Case 5: All same elements
    arr = [5, 5, 5, 5, 5]
    print(f"Test 5 - Most frequent: {most_frequent(arr)}")  # Expected: 5

    # Test Case 6: Empty array
    arr = []
    print(f"Test 6 - Most frequent: {most_frequent(arr)}")  # Expected: None

    # Test Case 7: Single element
    arr = [42]
    print(f"Test 7 - Most frequent: {most_frequent(arr)}")  # Expected: 42

    # Test Case 8: With count
    arr = [1, 3, 2, 1, 4, 1]
    element, count = most_frequent_with_count(arr)
    print(f"Test 8 - Most frequent: {element}, Count: {count}")  # Expected: 1, 3

    # Test Case 9: Top k frequent
    arr = [1, 1, 1, 2, 2, 3, 3, 3, 4]
    print(f"Test 9 - Top 2 frequent: {top_k_frequent(arr, 2)}")
    # Expected: [(1, 3), (3, 3)] or [(3, 3), (1, 3)]

    # Test Case 10: Least frequent
    arr = [1, 1, 2, 2, 3, 4, 5]
    print(
        f"Test 10 - Least frequent: {sorted(least_frequent(arr))}"
    )  # Expected: [3, 4, 5]

    # Test Case 11: Frequency distribution
    arr = [1, 2, 2, 3, 3, 3]
    print(f"Test 11 - Distribution: {frequency_distribution(arr)}")
    # Expected: {1: 1, 2: 2, 3: 3}
