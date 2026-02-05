"""
Lexicographically Next String

Given a string s, find the smallest string that is strictly greater than s
in lexicographic order.

Approach: Greedy Rightmost Increment - O(n) Time and O(1) Space
Scan from right to left, find first non-'z' character and increment it.
"""


def next_string(s):
    """
    Find the lexicographically next string.

    Args:
        s: Input string

    Returns:
        Next lexicographic string
    """
    i = len(s) - 1

    # Move left while characters are 'z'
    while i >= 0 and s[i] == "z":
        i -= 1

    # If all characters were 'z', append 'a'
    if i == -1:
        return s + "a"

    # Increment the rightmost non-'z' character
    arr = list(s)
    arr[i] = chr(ord(arr[i]) + 1)

    # Return only up to the incremented character
    return "".join(arr[: i + 1])


def main():
    """Test cases for lexicographically next string."""
    test_cases = [
        ("geeks", "geekt"),
        ("raavz", "raaw"),
        ("zzz", "zzza"),
        ("abc", "abd"),
        ("xy", "xz"),
    ]

    print("=" * 50)
    print("Lexicographically Next String")
    print("=" * 50)

    for s, expected in test_cases:
        result = next_string(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}' {status}")


if __name__ == "__main__":
    main()
