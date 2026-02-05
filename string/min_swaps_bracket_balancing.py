"""
Minimum Swaps for Bracket Balancing

Given a string of '[' and ']' brackets, find minimum adjacent swaps
to make the string balanced.

Approach: Imbalance Counting Method - O(n) Time and O(1) Space
Count imbalance and calculate swaps needed when encountering opening brackets.
"""


def min_swaps_bracket_balancing(s):
    """
    Find minimum adjacent swaps to balance brackets.

    Args:
        s: String containing '[' and ']' brackets

    Returns:
        Minimum number of swaps
    """
    count_left = 0
    count_right = 0
    swaps = 0
    imbalance = 0

    for char in s:
        if char == "[":
            count_left += 1
            if imbalance > 0:
                swaps += imbalance
                imbalance -= 1
        else:  # char == ']'
            count_right += 1
            imbalance = count_right - count_left

    return swaps


def main():
    """Test cases for minimum swaps bracket balancing."""
    test_cases = [
        ("[]][][", 2),
        ("[[][]]", 0),
        ("[][][]", 0),
        ("]]][[[", 3),
        ("[][]][", 1),
    ]

    print("=" * 50)
    print("Minimum Swaps for Bracket Balancing")
    print("=" * 50)

    for s, expected in test_cases:
        result = min_swaps_bracket_balancing(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Min Swaps: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
