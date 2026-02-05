"""
Reverse a String using Recursion
https://www.geeksforgeeks.org/dsa/reverse-a-string-using-recursion/

Given a string, print the string in reverse order using recursion.

Examples:
Input: s = "Geeks for Geeks"
Output: "skeeG rof skeeG"

Approach: Make recursive call for substring starting from second character,
then append the first character.

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n), due to recursion stack
"""


def reverse_string(s):
    """
    Reverse a string using recursion.

    Args:
        s: Input string

    Returns:
        Reversed string
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s

    # Recursive case: reverse(substring from index 1) + first character
    return reverse_string(s[1:]) + s[0]


def reverse_string_in_place(s_list, start, end):
    """
    Reverse a string in-place using recursion (two-pointer approach).

    Args:
        s_list: List of characters (strings are immutable in Python)
        start: Starting index
        end: Ending index
    """
    # Base case: pointers crossed
    if start >= end:
        return

    # Swap characters at start and end
    s_list[start], s_list[end] = s_list[end], s_list[start]

    # Recursive call with updated pointers
    reverse_string_in_place(s_list, start + 1, end - 1)


def main():
    """Test the reverse_string function with various inputs."""
    test_cases = [
        "Geeks for Geeks",
        "Reverse a string Using Recursion",
        "Hello",
        "A",
        "",
    ]

    print("=" * 60)
    print("Reverse a String using Recursion")
    print("=" * 60)

    print("\nApproach 1: Creating new string")
    print("-" * 60)
    for s in test_cases:
        reversed_str = reverse_string(s)
        print(f'\nInput:  "{s}"')
        print(f'Output: "{reversed_str}"')

    print("\n" + "=" * 60)
    print("Approach 2: In-place reversal (using list)")
    print("-" * 60)
    for s in test_cases:
        if s:  # Skip empty string for in-place
            char_list = list(s)
            reverse_string_in_place(char_list, 0, len(char_list) - 1)
            reversed_str = "".join(char_list)
            print(f'\nInput:  "{s}"')
            print(f'Output: "{reversed_str}"')

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
