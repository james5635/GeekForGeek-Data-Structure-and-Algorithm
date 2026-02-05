"""
Count Substrings Start and End with 1

Problem: Given a binary string, count the number of substrings that
start and end with 1.

Examples:
- Input: "00100101", Output: 3
  Explanation: Substrings are "1001", "100101", "101"
- Input: "111", Output: 6
  Explanation: Substrings are "11"(0,1), "11"(1,2), "111", "1"(0), "1"(1), "1"(2)

Time Complexity: O(n) where n is length of string
Space Complexity: O(1)
"""


def count_substrings_start_end_1(s: str) -> int:
    """
    Count substrings that start and end with 1.

    If there are n occurrences of '1', then number of valid substrings
    is n * (n + 1) / 2 (combinations of choosing 2 positions from n).

    Args:
        s: Binary string

    Returns:
        Count of substrings starting and ending with 1
    """
    # Count occurrences of '1'
    count_ones = s.count("1")

    # Number of ways to choose 2 positions from count_ones
    # Plus single character '1's (which also count)
    return count_ones * (count_ones + 1) // 2


def count_substrings_brute_force(s: str) -> int:
    """
    Brute force approach - check all possible substrings.

    Args:
        s: Binary string

    Returns:
        Count of substrings starting and ending with 1
    """
    count = 0
    n = len(s)

    for i in range(n):
        if s[i] == "1":
            for j in range(i, n):
                if s[j] == "1":
                    count += 1

    return count


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("00100101", 3),
        ("111", 6),
        ("000", 0),
        ("1", 1),
        ("11", 3),
        ("101", 3),
        ("10101", 6),
        ("", 0),
        ("0001000", 1),
    ]

    print("=" * 60)
    print("Count Substrings Start and End with 1 - Test Results")
    print("=" * 60)

    for s, expected in test_cases:
        result = count_substrings_start_end_1(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{s}' | Expected: {expected} | Got: {result} | {status}")

    print("=" * 60)

    # Verify with brute force
    print("\nVerifying with brute force approach:")
    for s, expected in test_cases:
        result_bf = count_substrings_brute_force(s)
        result_opt = count_substrings_start_end_1(s)
        match = "MATCH" if result_bf == result_opt else "MISMATCH"
        print(
            f"Input: '{s}' | Brute Force: {result_bf} | Optimized: {result_opt} | {match}"
        )
