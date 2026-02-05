"""
Recaman's Sequence

Problem Description:
    Print first n elements of Recaman's sequence.
    Recaman's sequence starts with 0, and each subsequent term is:
    - previous term - index (if positive and not already in sequence)
    - previous term + index (otherwise)

Approach:
    Use hash set to track visited numbers for O(1) lookup.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Set


def recaman_sequence(n: int) -> List[int]:
    """
    Generate first n elements of Recaman's sequence.

    Args:
        n: Number of elements to generate

    Returns:
        List of first n Recaman's sequence elements
    """
    if n <= 0:
        return []

    sequence = [0] * n
    seen = {0}

    for i in range(1, n):
        prev = sequence[i - 1]
        # Try subtracting first
        candidate = prev - i

        # If candidate is negative or already seen, add instead
        if candidate < 0 or candidate in seen:
            candidate = prev + i

        sequence[i] = candidate
        seen.add(candidate)

    return sequence


def recaman_sequence_optimized(n: int) -> List[int]:
    """
    Optimized version using list for seen array when n is small.

    Time Complexity: O(n)
    Space Complexity: O(max_value) where max_value can be O(n^2)
    """
    if n <= 0:
        return []

    # Estimate maximum value (can be O(n^2) in worst case)
    max_possible = n * (n + 1) // 2 + 1
    seen = [False] * (max_possible + 1)

    sequence = [0] * n
    seen[0] = True

    for i in range(1, n):
        prev = sequence[i - 1]
        candidate = prev - i

        if candidate < 0 or (candidate <= max_possible and seen[candidate]):
            candidate = prev + i

        sequence[i] = candidate
        if candidate <= max_possible:
            seen[candidate] = True

    return sequence


def is_in_recaman(x: int, max_n: int = 100000) -> bool:
    """
    Check if a number x appears in Recaman's sequence within first max_n terms.

    Args:
        x: Number to search for
        max_n: Maximum number of terms to check

    Returns:
        True if x appears in sequence, False otherwise
    """
    seen = set()
    current = 0
    seen.add(current)

    if x == 0:
        return True

    for i in range(1, max_n):
        candidate = current - i
        if candidate < 0 or candidate in seen:
            candidate = current + i

        if candidate == x:
            return True

        seen.add(candidate)
        current = candidate

    return False


def first_occurrence_in_recaman(x: int, max_n: int = 100000) -> int:
    """
    Find the first index where x appears in Recaman's sequence.

    Returns:
        Index of first occurrence, or -1 if not found within max_n terms
    """
    seen = set()
    current = 0
    seen.add(current)

    if x == 0:
        return 0

    for i in range(1, max_n):
        candidate = current - i
        if candidate < 0 or candidate in seen:
            candidate = current + i

        if candidate == x:
            return i

        seen.add(candidate)
        current = candidate

    return -1


def test_recaman():
    """Test cases for Recaman's sequence."""
    test_cases = [
        # (n, expected_sequence)
        (6, [0, 1, 3, 6, 2, 7]),
        (17, [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8]),
        (1, [0]),
        (2, [0, 1]),
        (0, []),
    ]

    print("Running test cases for Recaman's Sequence:")
    print("=" * 60)

    for i, (n, expected) in enumerate(test_cases, 1):
        result = recaman_sequence(n)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}: n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")

    # Test first occurrence
    print("\nTest first occurrence of numbers:")
    test_nums = [0, 1, 2, 3, 5, 8, 13, 21]
    for num in test_nums:
        idx = first_occurrence_in_recaman(num)
        print(f"  {num} first appears at index {idx}")


if __name__ == "__main__":
    # Example usage
    n = 17
    sequence = recaman_sequence(n)

    print(f"First {n} elements of Recaman's sequence:")
    print(sequence)
    print()

    print("First 50 elements:")
    print(recaman_sequence(50))
    print()

    # Run tests
    test_recaman()
