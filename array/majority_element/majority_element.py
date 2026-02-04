"""
Majority Element

An element is called a majority element if it appears more than n/2 times
in an array of size n.

Approaches:
1. Naive: Count each element - O(n²) time, O(1) space
2. Better: Sort and check middle - O(n log n) time, O(1) or O(n) space
3. Optimal: Moore's Voting Algorithm - O(n) time, O(1) space
4. Verify: Check if candidate is majority - O(n) time
"""


def majority_element_naive(arr):
    """
    Naive approach: Count occurrences of each element.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each element, count its occurrences in the array
    - Return element if count > n/2

    Args:
        arr: List of integers

    Returns:
        Majority element if exists, otherwise -1
    """
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1
        if count > n // 2:
            return arr[i]
    return -1


def majority_element_sort(arr):
    """
    Better approach: Sort and check middle element.

    Time Complexity: O(n log n)
    Space Complexity: O(1) if in-place, O(n) otherwise

    Algorithm:
    - Sort the array
    - If majority exists, it must be at index n//2
    - Verify by counting occurrences

    Args:
        arr: List of integers

    Returns:
        Majority element if exists, otherwise -1
    """
    if not arr:
        return -1

    n = len(arr)
    sorted_arr = sorted(arr)
    candidate = sorted_arr[n // 2]

    # Verify the candidate
    count = sum(1 for x in arr if x == candidate)
    return candidate if count > n // 2 else -1


def majority_element_moore_voting(arr):
    """
    Optimal approach: Boyer-Moore Voting Algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Maintain a candidate and count
    - When count is 0, pick current element as candidate
    - Increment count if current == candidate, else decrement
    - Candidate is the potential majority element

    Key Insight:
    If we cancel out each occurrence of an element with all other elements
    that are different, the majority element will still remain.

    Args:
        arr: List of integers

    Returns:
        Majority element if exists, otherwise -1
    """
    if not arr:
        return -1

    # Phase 1: Find candidate
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify candidate
    count = sum(1 for x in arr if x == candidate)
    return candidate if count > len(arr) // 2 else -1


def moore_voting_with_verification(arr):
    """
    Moore's Voting Algorithm with separate verification.

    Returns tuple of (candidate, is_majority)
    """
    if not arr:
        return -1, False

    # Find candidate
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify
    count = sum(1 for x in arr if x == candidate)
    is_majority = count > len(arr) // 2

    return candidate, is_majority


def majority_element_hashmap(arr):
    """
    Alternative: Using hash map to count frequencies.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Good for understanding, but Moore's is preferred.
    """
    from collections import Counter

    if not arr:
        return -1

    n = len(arr)
    counts = Counter(arr)

    for num, count in counts.items():
        if count > n // 2:
            return num
    return -1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [3, 3, 4, 2, 4, 4, 2, 4, 4],
        [3, 3, 4, 2, 4, 4, 2, 4],
        [1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5],
        [2, 2, 2, 2, 2, 2],
        [1],
        [1, 2],
        [2, 2],
    ]

    print("=" * 70)
    print("Majority Element (appears more than n/2 times)")
    print("=" * 70)
    print("\nFind element that appears more than n/2 times.\n")

    for i, arr in enumerate(test_cases, 1):
        naive_result = majority_element_naive(arr)
        sort_result = majority_element_sort(arr)
        moore_result = majority_element_moore_voting(arr)
        hashmap_result = majority_element_hashmap(arr)

        match = (
            "✓"
            if naive_result == sort_result == moore_result == hashmap_result
            else "✗"
        )

        print(f"Test {i}: arr = {arr}")
        print(f"  Naive O(n²):              {naive_result}")
        print(f"  Sort O(n log n):          {sort_result}")
        print(f"  Moore's O(n):             {moore_result}")
        print(f"  Hashmap O(n):             {hashmap_result} {match}")
        print()

    print("=" * 70)
    print("\nBoyer-Moore Voting Algorithm Explanation:")
    print("  Phase 1 - Find Candidate:")
    print("    - When count=0, pick current as candidate")
    print("    - Increment if same, decrement if different")
    print("  Phase 2 - Verify:")
    print("    - Count occurrences of candidate")
    print("    - Return if count > n/2, else -1")
    print("\n  Key Insight: Cancel out pairs of different elements")
    print("  Time: O(n), Space: O(1)")
    print("=" * 70)
