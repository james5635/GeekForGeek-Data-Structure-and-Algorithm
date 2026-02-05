"""
Sort Strings by Length

Problem Description:
    Given an array of strings, sort the array according to the length of
    the strings. If two strings have the same length, maintain their relative
    order (stable sort).

Algorithm:
    - Use Python's built-in sort with key=len
    - Python's sort is stable, so equal-length strings maintain order
    - Alternative: Use counting sort if lengths are bounded

Time Complexity: O(n log n * m)
    - n: number of strings
    - m: average length of strings
    - Sorting: O(n log n)
    - Length calculation: O(m) per string

Space Complexity: O(n)
    - For storing sorted array
"""


def sort_by_length_builtin(strings):
    """
    Sort strings by length using built-in sort.

    Args:
        strings: List of strings

    Returns:
        list: Sorted list of strings
    """
    return sorted(strings, key=len)


def sort_by_length_descending(strings):
    """
    Sort strings by length in descending order.

    Args:
        strings: List of strings

    Returns:
        list: Sorted list of strings (longest first)
    """
    return sorted(strings, key=len, reverse=True)


def sort_by_length_counting(strings, max_length=1000):
    """
    Sort strings by length using counting sort.
    Efficient when max length is known and small.

    Args:
        strings: List of strings
        max_length: Maximum possible string length

    Returns:
        list: Sorted list of strings
    """
    if not strings:
        return strings

    # Create buckets for each possible length
    buckets = [[] for _ in range(max_length + 1)]

    # Place strings in appropriate buckets
    for s in strings:
        length = len(s)
        if length <= max_length:
            buckets[length].append(s)

    # Concatenate all buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def sort_by_length_then_alphabetical(strings):
    """
    Sort by length first, then alphabetically for same length.

    Args:
        strings: List of strings

    Returns:
        list: Sorted list of strings
    """
    return sorted(strings, key=lambda x: (len(x), x.lower()))


def group_by_length(strings):
    """
    Group strings by their lengths.

    Args:
        strings: List of strings

    Returns:
        dict: Dictionary with lengths as keys, lists of strings as values
    """
    from collections import defaultdict

    groups = defaultdict(list)
    for s in strings:
        groups[len(s)].append(s)

    return dict(sorted(groups.items()))


if __name__ == "__main__":
    # Test Case 1: Basic case
    strings1 = ["apple", "pie", "banana", "cat", "dog", "elephant"]
    print(f"Original: {strings1}")
    print(f"Sorted by length: {sort_by_length_builtin(strings1.copy())}")
    print()

    # Test Case 2: Same length strings
    strings2 = ["cat", "dog", "bat", "rat"]
    print(f"Original: {strings2}")
    print(f"Sorted (stable): {sort_by_length_builtin(strings2.copy())}")
    print()

    # Test Case 3: Descending order
    strings3 = ["a", "bb", "ccc", "dddd", "eeeee"]
    print(f"Original: {strings3}")
    print(f"Sorted (descending): {sort_by_length_descending(strings3.copy())}")
    print()

    # Test Case 4: Empty strings
    strings4 = ["hello", "", "world", "a", ""]
    print(f"Original: {strings4}")
    print(f"Sorted: {sort_by_length_builtin(strings4.copy())}")
    print()

    # Test Case 5: Single character strings
    strings5 = ["z", "a", "m", "b"]
    print(f"Original: {strings5}")
    print(f"Sorted: {sort_by_length_builtin(strings5.copy())}")
    print()

    # Test Case 6: Empty list
    strings6 = []
    print(f"Original: {strings6}")
    print(f"Sorted: {sort_by_length_builtin(strings6.copy())}")
    print()

    # Test Case 7: Counting sort approach
    strings7 = ["programming", "is", "fun", "and", "educational"]
    print(f"Original: {strings7}")
    print(
        f"Sorted (counting): {sort_by_length_counting(strings7.copy(), max_length=20)}"
    )
    print()

    # Test Case 8: Sort by length then alphabetical
    strings8 = ["banana", "apple", "cherry", "date", "fig"]
    print(f"Original: {strings8}")
    print(
        f"Sorted (length + alpha): {sort_by_length_then_alphabetical(strings8.copy())}"
    )
    print()

    # Test Case 9: Group by length
    strings9 = ["one", "two", "three", "four", "five", "six"]
    print(f"Original: {strings9}")
    print(f"Grouped by length: {group_by_length(strings9.copy())}")
    print()

    # Test Case 10: Mixed case
    strings10 = ["Geeks", "for", "Geeks", "is", "a", "platform", "for", "Geeks"]
    print(f"Original: {strings10}")
    print(f"Sorted: {sort_by_length_builtin(strings10.copy())}")
