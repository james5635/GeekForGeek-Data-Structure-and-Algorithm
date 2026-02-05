"""
Remove All Adjacent Duplicates in String

Given a string S of lowercase letters, remove all adjacent duplicates.
The result should have no adjacent duplicates.

Approach: Using Stack - O(n) Time and O(n) Space
Use a stack to keep track of characters and remove adjacent duplicates.
"""


def remove_adjacent_duplicates(s):
    """
    Remove all adjacent duplicate characters from string.

    Args:
        s: Input string

    Returns:
        String with adjacent duplicates removed
    """
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


def main():
    """Test cases for removing adjacent duplicates."""
    test_cases = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("abcddcba", ""),
        ("abccba", ""),
        ("aaaa", ""),
        ("abcdef", "abcdef"),
    ]

    print("=" * 50)
    print("Remove Adjacent Duplicates")
    print("=" * 50)

    for s, expected in test_cases:
        result = remove_adjacent_duplicates(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}' {status}")


if __name__ == "__main__":
    main()
