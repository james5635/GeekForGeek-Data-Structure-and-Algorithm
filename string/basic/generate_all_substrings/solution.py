"""
Generate All Substrings

Problem Description:
Generate all possible substrings of a given string.

Time Complexity: O(n^2) where n is the length of the string
Space Complexity: O(n^2) - To store all substrings

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
            substrings.append((s[i:j], i, j - 1))

    return substrings


def print_all_substrings(s: str) -> None:
    """
    Print all substrings in a formatted way.

    Args:
        s: Input string
    """
    print(f"All substrings of '{s}':")
    substrings = generate_all_substrings_with_indices(s)

    for substring, start, end in substrings:
        print(f"  '{substring}' (indices {start}-{end})")


def main():
    """Test cases for generate_all_substrings functions."""
    test_cases = [
        "abc",
        "a",
        "",
        "ab",
        "hello",
    ]

    print("Testing generate_all_substrings function:")
    for i, test_str in enumerate(test_cases):
        print(f"\nTest {i + 1}: '{test_str}'")
        substrings = generate_all_substrings(test_str)
        print(f"Number of substrings: {len(substrings)}")
        print(f"Substrings: {substrings}")

    print("\n" + "=" * 50)
    print("Detailed substring analysis:")
    for test_str in test_cases:
        if test_str:  # Skip empty string for detailed view
            print_all_substrings(test_str)
            print()


if __name__ == "__main__":
    main()
