"""
Find the First Repeated Character in a String

Given a string S of length n, find the earliest repeated character in it.
The earliest repeated character means, the character that occurs more than once
and whose second occurrence has the smallest index.

Approach: Using Frequency Counting - O(n) time and O(1) auxiliary space
We create an array of size 26 to store the count of each character.
For each character in the string, we check if it has appeared before.
"""


def first_repeated_char(s):
    """
    Find the first repeated character in a string.

    Args:
        s: Input string containing lowercase English letters

    Returns:
        First repeated character or "-1" if no repetition
    """
    char_count = [0] * 26

    for ch in s:
        index = ord(ch) - ord("a")

        if char_count[index] != 0:
            return ch

        char_count[index] += 1

    return "-1"


def main():
    """Test cases for first repeated character."""
    test_cases = [
        ("geeksforgeeks", "e"),
        ("hello geeks", "l"),
        ("abcdef", "-1"),
        ("aabbcc", "a"),
    ]

    print("=" * 50)
    print("Find First Repeated Character")
    print("=" * 50)

    for s, expected in test_cases:
        result = first_repeated_char(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}' {status}")


if __name__ == "__main__":
    main()
