"""
Pangram Checking
Check if a given string is a pangram (contains all letters of the alphabet).

Approach: Use a boolean array to mark visited characters
Time Complexity: O(n), where n is the length of the string
Auxiliary Space: O(1) - fixed size array of 26
"""


def is_pangram(s: str) -> bool:
    """
    Check if the given string is a pangram.

    Args:
        s: Input string to check

    Returns:
        True if string contains all 26 letters, False otherwise
    """
    MAX_CHAR = 26
    visited = [False] * MAX_CHAR

    for char in s:
        if "A" <= char <= "Z":
            visited[ord(char) - ord("A")] = True
        elif "a" <= char <= "z":
            visited[ord(char) - ord("a")] = True

    # Check if all characters were visited
    for flag in visited:
        if not flag:
            return False

    return True


def main():
    """Test the pangram checker with various inputs."""
    test_cases = [
        ("The quick brown fox jumps over the lazy dog", True),
        ("The quick brown fox jumps over the dog", False),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("Hello World", False),
        ("Pack my box with five dozen liquor jugs", True),
        ("", False),
    ]

    print("Pangram Checking")
    print("=" * 70)

    for s, expected in test_cases:
        result = is_pangram(s)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        # Show only first 50 chars of input for readability
        display_s = s[:50] + "..." if len(s) > 50 else s
        print(f"{status} | Input: '{display_s}'")
        print(f"       | Expected: {expected} | Got: {result}")
        print()


if __name__ == "__main__":
    main()
