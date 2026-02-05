"""
Find the Length of a String
============================

Problem Description:
--------------------
Given a string, find its length without using built-in len() function.

Approaches:
-----------
1. Iterative: Count characters one by one
2. Using enumerate: Get last index + 1

Time Complexity: O(n) where n is the length of string
Space Complexity: O(1)

Reference: https://www.geeksforgeeks.org/dsa/find-the-length-of-a-string/
"""


def find_length_iterative(s: str) -> int:
    """Find length by iterating through string."""
    count = 0
    for _ in s:
        count += 1
    return count


def find_length_enumerate(s: str) -> int:
    """Find length using enumerate."""
    length = 0
    for i, _ in enumerate(s):
        length = i + 1
    return length


def test_find_length():
    """Test cases for find length function."""
    test_cases = [
        ("Hello World", 11),
        ("", 0),
        ("a", 1),
        ("Python", 6),
        ("12345", 5),
        ("  spaces  ", 10),
    ]

    print("Testing find_length_iterative:")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = find_length_iterative(input_str)
        status = "✓" if result == expected else "✗"
        print(
            f"  Test {i}: {status} Input: '{input_str}' -> {result} (expected: {expected})"
        )

    print("\nTesting find_length_enumerate:")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = find_length_enumerate(input_str)
        status = "✓" if result == expected else "✗"
        print(
            f"  Test {i}: {status} Input: '{input_str}' -> {result} (expected: {expected})"
        )


if __name__ == "__main__":
    test_find_length()
