"""
URLify String

Problem: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
the additional characters.

Examples:
- Input: "Mr John Smith    ", length = 13
  Output: "Mr%20John%20Smith"
- Input: "hello world  ", length = 11
  Output: "hello%20world"

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for the result string
"""


def urlify(s: str, true_length: int) -> str:
    """
    Replace all spaces with '%20'.

    Args:
        s: Input string with extra space at end
        true_length: True length of the string (without trailing spaces)

    Returns:
        URLified string
    """
    result = []

    for i in range(true_length):
        if s[i] == " ":
            result.append("%20")
        else:
            result.append(s[i])

    return "".join(result)


def urlify_pythonic(s: str, true_length: int = None) -> str:
    """
    Pythonic way using replace method.

    Args:
        s: Input string
        true_length: True length (optional in Python)

    Returns:
        URLified string
    """
    if true_length is not None:
        s = s[:true_length]
    return s.replace(" ", "%20")


def urlify_in_place(s: list, true_length: int) -> str:
    """
    In-place modification approach (simulated with list).
    This is how you'd do it in languages with mutable strings.

    Args:
        s: List of characters (mutable)
        true_length: True length of string

    Returns:
        URLified string
    """
    # Count spaces
    space_count = sum(1 for i in range(true_length) if s[i] == " ")

    # Calculate new length
    new_length = true_length + space_count * 2

    # Extend list if needed
    while len(s) < new_length:
        s.append("")

    # Fill from end
    index = new_length - 1

    for i in range(true_length - 1, -1, -1):
        if s[i] == " ":
            s[index] = "0"
            s[index - 1] = "2"
            s[index - 2] = "%"
            index -= 3
        else:
            s[index] = s[i]
            index -= 1

    return "".join(s)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("hello world  ", 11, "hello%20world"),
        ("a b c", 5, "a%20b%20c"),
        ("nospaces", 8, "nospaces"),
        ("  ", 1, "%20"),
        ("", 0, ""),
        (" single", 7, "%20single"),
        ("single ", 7, "single%20"),
    ]

    print("=" * 70)
    print("URLify String - Test Results")
    print("=" * 70)

    for s, length, expected in test_cases:
        result = urlify(s, length)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{s}' | Length: {length}")
        print(f"Expected: '{expected}' | Got: '{result}' | {status}")
        print("-" * 70)

    print("=" * 70)

    # Compare implementations
    print("\nComparing implementations:")
    print("-" * 70)
    for s, length, expected in test_cases[:5]:
        r1 = urlify(s, length)
        r2 = urlify_pythonic(s, length)
        all_match = r1 == r2 == expected
        status = "PASS" if all_match else "FAIL"
        print(f"Input: '{s[:20]}...' | Manual: '{r1}' | Pythonic: '{r2}' | {status}")

    # Test in-place version
    print("\nTesting in-place version:")
    s_list = list("Mr John Smith    ")
    result = urlify_in_place(s_list, 13)
    print(f"In-place: '{result}'")
