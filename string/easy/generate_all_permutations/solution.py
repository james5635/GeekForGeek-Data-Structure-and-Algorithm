"""
Generate All Permutations of a String

Generate all possible permutations of characters in a given string.

Time Complexity: O(n!), where n is the length of the string
Space Complexity: O(n!) for storing all permutations

Examples:
- Input: "abc", Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
- Input: "ab", Output: ["ab", "ba"]
- Input: "a", Output: ["a"]
- Input: "", Output: [""]
"""


def generate_permutations(s: str) -> list[str]:
    """
    Generate all permutations of a string using backtracking.

    Args:
        s: Input string

    Returns:
        List of all permutations of the input string
    """
    if not s:
        return [""]

    # Convert string to list for easier manipulation
    chars = list(s)
    result = []

    def backtrack(start: int):
        """Recursive backtracking function."""
        if start == len(chars) - 1:
            result.append("".join(chars))
            return

        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]

            # Recurse
            backtrack(start + 1)

            # Backtrack - restore original order
            chars[start], chars[i] = chars[i], chars[start]

    backtrack(0)
    return result


def generate_permutations_with_duplicates(s: str) -> list[str]:
    """
    Generate all permutations of a string, handling duplicate characters.
    Uses a set to avoid duplicate permutations.

    Args:
        s: Input string

    Returns:
        List of unique permutations of the input string
    """
    if not s:
        return [""]

    # Sort characters to handle duplicates efficiently
    chars = sorted(s)
    result = []
    used = [False] * len(chars)

    def backtrack(current: list[str]):
        """Recursive backtracking function with duplicate handling."""
        if len(current) == len(chars):
            result.append("".join(current))
            return

        for i in range(len(chars)):
            # Skip if character is already used
            if used[i]:
                continue

            # Skip duplicates: if current character is same as previous
            # and previous hasn't been used in this position
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue

            # Choose character
            used[i] = True
            current.append(chars[i])

            # Recurse
            backtrack(current)

            # Backtrack
            current.pop()
            used[i] = False

    backtrack([])
    return result


def generate_permutations_iterative(s: str) -> list[str]:
    """
    Generate all permutations using an iterative approach.

    Args:
        s: Input string

    Returns:
        List of all permutations of the input string
    """
    if not s:
        return [""]

    result = [""]

    for char in s:
        new_result = []
        for perm in result:
            # Insert current character at every possible position
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + char + perm[i:]
                new_result.append(new_perm)
        result = new_result

    return result


def test_generate_permutations():
    """Test cases for generate_permutations function."""
    test_cases = [
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("", [""]),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = generate_permutations(input_str)
        assert set(result) == set(expected), (
            f"Test case {i} failed: generate_permutations('{input_str}') = {result}, expected {expected}"
        )

    # Test with duplicates
    result_duplicates = generate_permutations_with_duplicates("aab")
    expected_duplicates = ["aab", "aba", "baa"]
    assert set(result_duplicates) == set(expected_duplicates), (
        f"Duplicate test failed: {result_duplicates}"
    )

    print("All test cases passed!")


def test_permutations_consistency():
    """Test that different implementations produce same results."""
    test_strings = ["abc", "ab", "a"]

    for s in test_strings:
        result1 = generate_permutations(s)
        result2 = generate_permutations_iterative(s)
        assert set(result1) == set(result2), f"Consistency test failed for '{s}'"

    print("Consistency tests passed!")


if __name__ == "__main__":
    # Example usage
    test_strings = ["abc", "aab", ""]

    print("String Permutations:")
    for s in test_strings:
        print(f"\nPermutations of '{s}':")
        if s and len(set(s)) == len(s):  # No duplicates
            perms = generate_permutations(s)
        else:  # Has duplicates
            perms = generate_permutations_with_duplicates(s)

        for i, perm in enumerate(perms, 1):
            print(f"  {i}. {perm}")
        print(f"Total: {len(perms)} permutations")

    print("\nTesting iterative approach for 'abc':")
    iterative_perms = generate_permutations_iterative("abc")
    for i, perm in enumerate(iterative_perms, 1):
        print(f"  {i}. {perm}")

    print("\nRunning tests...")
    test_generate_permutations()
    test_permutations_consistency()
