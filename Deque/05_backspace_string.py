from collections import deque


def process_backspace_string(s):
    """
    Process string with backspace characters using deque.

    Approach:
    - Use deque to efficiently add/remove from both ends
    - When '#' is encountered, pop from the end (simulating backspace)
    - Process character by character, building final result

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        s: Input string with possible '#' characters

    Returns:
        Processed string after backspace
    """
    if not s:
        return ""

    result = deque()

    for char in s:
        if char == "#":
            if result:
                result.pop()
        else:
            result.append(char)

    return "".join(result)


def process_backspace_string_two_pointer(s):
    """
    Two pointer approach without extra space.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not s:
        return ""

    result = []
    skip = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "#":
            skip += 1
        elif skip > 0:
            skip -= 1
        else:
            result.append(s[i])

    return "".join(reversed(result))


def process_backspace_strings_equal(s1, s2):
    """
    Check if two strings with backspace are equal using deque.

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    return process_backspace_string(s1) == process_backspace_string(s2)


def main():
    print("=== String After Processing Backspace ===\n")

    test_cases = [
        ("abc#de#f#ghi#jklmn#op#", "abdghjklmo"),
        ("##geeks##for##geeks#", "geefgeek"),
        ("ab#c", "ac"),
        ("###abc", "abc"),
        ("#####", ""),
        ("a###b", "b"),
        ("y#fo##fr", "fr"),
    ]

    for s, expected in test_cases:
        result = process_backspace_string(s)
        status = "✓" if result == expected else "✗"
        print(f'Input: "{s}"')
        print(f'Output: "{result}" (Expected: "{expected}") {status}')
        print()

    print("--- Two Pointer Approach ---")
    for s, expected in test_cases:
        result = process_backspace_string_two_pointer(s)
        status = "✓" if result == expected else "✗"
        print(f'Input: "{s}" → Output: "{result}" {status}')

    print("\n--- Equal Check Test ---")
    test_pairs = [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b#c", False),
    ]
    for s1, s2, expected in test_pairs:
        result = process_backspace_strings_equal(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f'"{s1}" == "{s2}" → {result} (Expected: {expected}) {status}')


if __name__ == "__main__":
    main()
