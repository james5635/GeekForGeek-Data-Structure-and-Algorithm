"""
Count Binary Substrings Starting and Ending with 1
Given a binary string, count all substrings that start and end with '1'.

Efficient Approach: Count number of 1's and use formula m*(m-1)/2
Time Complexity: O(n), where n is the length of the string
Auxiliary Space: O(1)
"""


def count_binary_substrings(s: str) -> int:
    """
    Count substrings that start and end with '1'.

    For every pair of '1's, one valid substring can be formed.
    If there are m '1's, total substrings = m*(m-1)/2

    Args:
        s: Binary string

    Returns:
        Count of valid substrings
    """
    ones_count = 0

    # Count all '1's in the string
    for char in s:
        if char == "1":
            ones_count += 1

    # Return total substrings using combination formula
    return (ones_count * (ones_count - 1)) // 2


def count_binary_substrings_brute_force(s: str) -> int:
    """
    Brute force approach - check all possible substrings.

    Time Complexity: O(n^2)
    """
    n = len(s)
    count = 0

    for i in range(n):
        if s[i] == "1":
            for j in range(i + 1, n):
                if s[j] == "1":
                    count += 1

    return count


def main():
    """Test the binary substring counter with various inputs."""
    test_cases = [
        ("00100101", 3),
        ("1001", 1),
        ("111", 3),
        ("000", 0),
        ("101010", 6),
        ("1", 0),
        ("11", 1),
    ]

    print("Count Binary Substrings (Start & End with 1)")
    print("=" * 60)

    for s, expected in test_cases:
        result = count_binary_substrings(s)
        brute_result = count_binary_substrings_brute_force(s)
        status = "✓ PASS" if result == expected and result == brute_result else "✗ FAIL"
        print(f"{status} | Input: '{s}'")
        print(f"       | Expected: {expected}")
        print(f"       | Efficient: {result}, Brute Force: {brute_result}")
        print()


if __name__ == "__main__":
    main()
