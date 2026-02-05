"""
Second Most Frequent Character

Find the second most frequent character in a string. If there are multiple characters
with the same frequency, return any one of them. If there's no second most frequent
character (all characters appear once or only one unique character), return appropriate message.

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(k), where k is the number of unique characters

Examples:
- Input: "aababbccd", Output: "a" (most frequent: 'b', second most: 'a' and 'c')
- Input: "test", Output: "No second most frequent character"
- Input: "aaaa", Output: "No second most frequent character"
- Input: "aabbbccc", Output: "a" or "c" (most frequent: 'b', second most: 'a' and 'c')
"""


def second_most_frequent_char(s: str) -> str:
    """
    Find the second most frequent character in a string.

    Args:
        s: Input string

    Returns:
        The second most frequent character, or an error message
    """
    if not s:
        return "No second most frequent character"

    # Count character frequencies
    char_count = {}
    for char in s:
        if char != " ":  # Ignore spaces (optional)
            char_count[char] = char_count.get(char, 0) + 1

    # If less than 2 unique characters, no second most frequent
    if len(char_count) < 2:
        return "No second most frequent character"

    # Sort characters by frequency (descending)
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Check if there's a distinct second frequency
    if len(sorted_chars) >= 2:
        # Find the highest frequency
        highest_freq = sorted_chars[0][1]

        # If highest frequency is 1, all characters appear once
        if highest_freq == 1:
            return "No second most frequent character"

        # Find characters with second highest frequency (distinct from highest)
        for i in range(1, len(sorted_chars)):
            if sorted_chars[i][1] < highest_freq:
                return sorted_chars[i][0]

        # All characters have same frequency
        return "No second most frequent character"

    return "No second most frequent character"


def second_most_frequent_char_with_ties(s: str) -> str:
    """
    Find the second most frequent character, handling ties properly.
    Returns any character with the second highest frequency.

    Args:
        s: Input string

    Returns:
        A character with the second highest frequency, or error message
    """
    if not s:
        return "No second most frequent character"

    # Count character frequencies
    char_count = {}
    for char in s:
        if char != " ":  # Ignore spaces
            char_count[char] = char_count.get(char, 0) + 1

    if len(char_count) < 2:
        return "No second most frequent character"

    # Get unique frequencies sorted in descending order
    frequencies = sorted(set(char_count.values()), reverse=True)

    if len(frequencies) < 2:
        return "No second most frequent character"

    second_highest_freq = frequencies[1]

    # Find all characters with the second highest frequency
    second_most_chars = [
        char for char, freq in char_count.items() if freq == second_highest_freq
    ]

    # Return any one of them
    return second_most_chars[0]


def second_most_frequent_char_full(s: str) -> str:
    """
    Comprehensive solution that returns all second most frequent characters.

    Args:
        s: Input string

    Returns:
        List of all characters with second highest frequency, or error message
    """
    if not s:
        return "No second most frequent character"

    # Count character frequencies
    char_count = {}
    for char in s:
        if char != " ":  # Ignore spaces
            char_count[char] = char_count.get(char, 0) + 1

    if len(char_count) < 2:
        return "No second most frequent character"

    # Get unique frequencies sorted in descending order
    frequencies = sorted(set(char_count.values()), reverse=True)

    if len(frequencies) < 2:
        return "No second most frequent character"

    second_highest_freq = frequencies[1]

    # Find all characters with the second highest frequency
    second_most_chars = [
        char for char, freq in char_count.items() if freq == second_highest_freq
    ]

    if not second_most_chars:
        return "No second most frequent character"

    # Return all characters joined as string
    return ", ".join(sorted(second_most_chars))


def test_second_most_frequent_char():
    """Test cases for second_most_frequent_char function."""
    test_cases = [
        (
            "aababbccd",
            "c",
        ),  # 'a' and 'b' are most frequent (3), 'c' is second most (2)
        ("test", ["e", "s"]),  # 't' is most frequent (2), 'e' and 's' are second (1)
        ("aaaa", "No second most frequent character"),  # Only one unique character
        (
            "aabbbccc",
            ["a", "c"],
        ),  # 'b' is most frequent (3), 'a' and 'c' are second (3) - actually tie
        ("aabbcc", "No second most frequent character"),  # All have same frequency
        ("a", "No second most frequent character"),
        ("", "No second most frequent character"),
        ("aabbbccdd", ["a", "c", "d"]),  # 'b' is most (3), others are second (2)
        (
            "abbbcdd",
            "d",
        ),  # 'b' is most (3), 'd' is second (2), 'a' and 'c' are third (1)
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = second_most_frequent_char(input_str)

        if isinstance(expected, list):
            assert result in expected, (
                f"Test case {i} failed: second_most_frequent_char('{input_str}') = '{result}', expected one of {expected}"
            )
        else:
            assert result == expected, (
                f"Test case {i} failed: second_most_frequent_char('{input_str}') = '{result}', expected '{expected}'"
            )

    print("All test cases passed!")


def test_ties_handling():
    """Test the ties handling function."""
    test_cases = [
        ("aabbbccc", ["a", "c"]),
        ("aabbccdd", "No second most frequent character"),
        ("aabbbc", "a"),
        ("test", ["e", "s"]),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = second_most_frequent_char_with_ties(input_str)

        if isinstance(expected, list):
            assert result in expected, (
                f"Ties test {i} failed: Got '{result}', expected one of {expected}"
            )
        else:
            assert result == expected, (
                f"Ties test {i} failed: Got '{result}', expected '{expected}'"
            )

    print("Ties handling tests passed!")


if __name__ == "__main__":
    # Example usage
    test_strings = ["aababbccd", "test", "aaaa", "aabbbccc", "aabbccdd", "aabbbccdd"]

    print("Second Most Frequent Character:")
    for s in test_strings:
        result = second_most_frequent_char(s)
        print(f"Input: '{s}' -> Second most frequent: '{result}'")

    print("\nWith ties handling:")
    for s in test_strings[:5]:
        result = second_most_frequent_char_with_ties(s)
        print(f"Input: '{s}' -> Second most frequent: '{result}'")

    print("\nFull solution (all second most frequent characters):")
    for s in test_strings[:5]:
        result = second_most_frequent_char_full(s)
        print(f"Input: '{s}' -> Second most frequent: {result}")

    print("\nRunning tests...")
    test_second_most_frequent_char()
    test_ties_handling()
