"""
K'th Non-Repeating Character

Given a string str and a number k, find the kth non-repeating character in the string.

Approach: Using Hashing - O(n) Time and O(n) Space
Create a hash map to store character counts, then find the kth character with count 1.
"""


def kth_non_repeating_char(s, k):
    """
    Find the kth non-repeating character in a string.

    Args:
        s: Input string
        k: The position of non-repeating character to find

    Returns:
        kth non-repeating character or None if doesn't exist
    """
    char_counts = {}

    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    non_repeating_count = 0
    for char in s:
        if char_counts[char] == 1:
            non_repeating_count += 1
            if non_repeating_count == k:
                return char

    return None


def main():
    """Test cases for kth non-repeating character."""
    test_cases = [
        ("geeksforgeeks", 3, "r"),
        ("geeksforgeeks", 2, "o"),
        ("geeksforgeeks", 4, None),
        ("abcdef", 1, "a"),
        ("aabbcc", 1, None),
    ]

    print("=" * 50)
    print("K'th Non-Repeating Character")
    print("=" * 50)

    for s, k, expected in test_cases:
        result = kth_non_repeating_char(s, k)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}', k = {k}")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
