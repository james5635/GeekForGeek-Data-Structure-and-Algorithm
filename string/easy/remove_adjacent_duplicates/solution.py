"""
Remove All Adjacent Duplicates

Remove all adjacent duplicate characters from a string. Keep removing until no more
adjacent duplicates can be removed.

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n) for the stack

Examples:
- Input: "abbaca", Output: "ca"
- Input: "azxxzy", Output: "ay"
- Input: "geeksforgeek", Output: "gfsor"
- Input: "abccbccba", Output: ""
"""


def remove_adjacent_duplicates(s: str) -> str:
    """
    Remove all adjacent duplicate characters from a string.
    Uses a stack-like approach to efficiently remove duplicates.

    Args:
        s: Input string

    Returns:
        String with all adjacent duplicates removed
    """
    if not s:
        return ""

    result = []

    for char in s:
        if result and result[-1] == char:
            # Remove the duplicate character
            result.pop()
        else:
            # Add character to the result
            result.append(char)

    return "".join(result)


def remove_adjacent_duplicates_recursive(s: str) -> str:
    """
    Alternative implementation using recursion.
    Less efficient but demonstrates the concept.

    Args:
        s: Input string

    Returns:
        String with all adjacent duplicates removed
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s

    # Find first pair of adjacent duplicates
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            # Remove the duplicate pair
            new_s = s[:i] + s[i + 2 :]
            # Recursively process the new string
            return remove_adjacent_duplicates_recursive(new_s)
        i += 1

    # No adjacent duplicates found
    return s


def remove_adjacent_duplicates_two_pass(s: str) -> str:
    """
    Implementation using two-pass approach.
    First pass removes obvious duplicates, second pass handles newly formed adjacent duplicates.

    Args:
        s: Input string

    Returns:
        String with all adjacent duplicates removed
    """
    changed = True
    current = s

    while changed:
        changed = False
        result = []
        i = 0

        while i < len(current):
            # Check for adjacent duplicates
            j = i + 1
            while j < len(current) and current[j] == current[i]:
                j += 1

            # If we found duplicates, skip them
            if j > i + 1:
                changed = True
            else:
                # No duplicates, keep the character
                result.append(current[i])

            i = j

        current = "".join(result)

    return current


def test_remove_adjacent_duplicates():
    """Test cases for remove_adjacent_duplicates function."""
    test_cases = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("geeksforgeek", "gksforgk"),
        ("abccbccba", "aba"),
        ("", ""),
        ("a", "a"),
        ("aa", ""),
        ("ab", "ab"),
        ("aabccbdd", ""),
        ("abbbbbcd", "abcd"),
        ("abcddcba", ""),
        ("acabbac", "a"),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = remove_adjacent_duplicates(input_str)
        assert result == expected, (
            f"Test case {i} failed: remove_adjacent_duplicates('{input_str}') = '{result}', expected '{expected}'"
        )

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    test_strings = ["abbaca", "azxxzy", "geeksforgeek", "abccbccba", "aabccbdd"]

    print("Remove Adjacent Duplicates:")
    for s in test_strings:
        result = remove_adjacent_duplicates(s)
        print(f"Input: '{s}' -> Output: '{result}'")

    print("\nTesting recursive implementation:")
    for s in test_strings[:3]:
        result = remove_adjacent_duplicates_recursive(s)
        print(f"Input: '{s}' -> Output: '{result}'")

    print("\nRunning tests...")
    test_remove_adjacent_duplicates()
