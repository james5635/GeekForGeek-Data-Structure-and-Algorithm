"""
Generate All Substrings

Problem Description:
Generate all possible substrings of a given string.

Time Complexity: O(n²) for generating all substrings
Space Complexity: O(n²) for storing all substrings

Implementation:
- Use nested loops to generate all substrings
- Outer loop for starting position, inner loop for ending position
"""


def generate_all_substrings(s: str) -> list[str]:
    """
    Generate all possible substrings of a string.

    Args:
        s: Input string

    Returns:
        List of all substrings
    """
    substrings = []
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])

    return substrings


def generate_all_substrings_with_indices(s: str) -> list[tuple[str, int, int]]:
    """
    Generate all substrings with their start and end indices.

    Args:
        s: Input string

    Returns:
        List of tuples (substring, start_index, end_index)
    """
    substrings = []
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append((s[i:j], i, j))

    return substrings


def generate_all_substrings_comprehension(s: str) -> list[str]:
    """
    Generate all substrings using list comprehension.

    Args:
        s: Input string

    Returns:
        List of all substrings
    """
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


def count_substrings(s: str) -> int:
    """
    Count the total number of possible substrings.

    Args:
        s: Input string

    Returns:
        Total number of substrings
    """
    n = len(s)
    return n * (n + 1) // 2


def test_generate_all_substrings():
    """Test cases for generate_all_substrings functions."""
    test_cases = [
        ("abc", ["a", "ab", "abc", "b", "bc", "c"]),
        ("a", ["a"]),
        ("", []),
        ("ab", ["a", "ab", "b"]),
        ("aa", ["a", "aa", "a"]),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        # Test basic method
        result1 = generate_all_substrings(input_str)
        assert result1 == expected, (
            f"Test case {i} failed (basic): input='{input_str}', expected={expected}, got={result1}"
        )

        # Test comprehension method
        result2 = generate_all_substrings_comprehension(input_str)
        assert result2 == expected, (
            f"Test case {i} failed (comprehension): input='{input_str}', expected={expected}, got={result2}"
        )

        # Test count function
        expected_count = len(expected)
        actual_count = count_substrings(input_str)
        assert actual_count == expected_count, (
            f"Test case {i} failed (count): input='{input_str}', expected={expected_count}, got={actual_count}"
        )

        print(f"Test case {i} passed: '{input_str}' -> {len(result1)} substrings")

    # Test with indices
    print("\nTesting substrings with indices:")
    test_str = "abc"
    result_with_indices = generate_all_substrings_with_indices(test_str)
    for substr, start, end in result_with_indices:
        print(f"  '{substr}' ({start}, {end})")


if __name__ == "__main__":
    test_generate_all_substrings()
    print("\nAll test cases passed!")
