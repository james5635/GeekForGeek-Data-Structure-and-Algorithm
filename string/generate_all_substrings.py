"""
Generate All Substrings of a String
GeeksforGeeks: https://www.geeksforgeeks.org/dsa/program-print-substrings-given-string/

Given a string s, containing lowercase alphabetical characters. The task is to
print all non-empty substrings of the given string.

A substring is any contiguous sequence of characters within the string.

Examples:
Input: s = "abc"
Output: "a", "ab", "abc", "b", "bc", "c"

Input: s = "ab"
Output: "a", "ab", "b"

Time Complexity: O(n^2) where n is length of string
Auxiliary Space: O(n^2) to store all substrings
"""


def find_all_substrings_iterative(s):
    """
    Find all substrings using nested loops (iterative approach).

    Args:
        s: Input string

    Returns:
        list: List of all substrings
    """
    res = []
    n = len(s)

    # Outer loop picks the starting index
    for i in range(n):
        # Inner loop picks the ending index
        for j in range(i, n):
            # Extract substring from index i to j (inclusive)
            res.append(s[i : j + 1])

    return res


def find_all_substrings_recursive(s):
    """
    Find all substrings using recursive approach.

    Args:
        s: Input string

    Returns:
        list: List of all substrings
    """
    res = []

    def substring_helper(index, cur):
        # If we have reached the end of the string
        if index == len(s):
            return

        # Add the character s[index] to the current string
        cur += s[index]

        # Add the current string in result
        res.append(cur)

        # Move to next index
        substring_helper(index + 1, cur)

        # Remove the current character from the current string
        cur = cur[:-1]

        # If current string is empty, skip the current index
        # to start the new substring
        if not cur:
            substring_helper(index + 1, cur)

    substring_helper(0, "")
    return res


def find_all_substrings_list_comprehension(s):
    """
    Find all substrings using list comprehension (Pythonic way).

    Args:
        s: Input string

    Returns:
        list: List of all substrings
    """
    return [s[i : j + 1] for i in range(len(s)) for j in range(i, len(s))]


if __name__ == "__main__":
    # Test cases
    test_strings = ["abc", "ab", "a", "xy", "code"]

    print("Generate All Substrings Demonstration")
    print("=" * 50)

    for s in test_strings:
        substrings_iterative = find_all_substrings_iterative(s)
        substrings_recursive = find_all_substrings_recursive(s)
        substrings_comprehension = find_all_substrings_list_comprehension(s)

        print(f"\nInput: '{s}'")
        print(f"Number of substrings: {len(substrings_iterative)}")
        print(f"Substrings (iterative): {' '.join(substrings_iterative)}")
        print(f"Substrings (recursive): {' '.join(substrings_recursive)}")
        print(f"Substrings (comprehension): {' '.join(substrings_comprehension)}")
        print(
            f"All methods match: {substrings_iterative == substrings_recursive == substrings_comprehension}"
        )
