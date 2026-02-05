"""
Recursively Remove Adjacent Duplicates from String

Given a string S, remove all its adjacent duplicate characters recursively.
This continues until no adjacent duplicates remain.

Examples:
- "geeksforgeek" -> "gksforgk"
- "abccbccba" -> "" (empty string)

Approach:
1. Iterate through the string and build a new string without adjacent duplicates
2. If duplicates were found, recursively call the function on the new string
3. If no duplicates were found, return the result

Time Complexity: O(n^2) - In worst case, need to iterate through entire string for each recursion
Auxiliary Space: O(n) - Due to recursive call stack
"""


def remove_util(s_list, n):
    """
    Helper function to remove adjacent duplicates.

    Args:
        s_list: List of characters (mutable)
        n: Length of current string

    Returns:
        Modified list of characters
    """
    # Index to store the result string
    k = 0

    # Iterate over the string to remove adjacent duplicates
    i = 0
    while i < n:
        # Check if the current character is the same as the next one
        if i < n - 1 and s_list[i] == s_list[i + 1]:
            # Skip all the adjacent duplicates
            while i < n - 1 and s_list[i] == s_list[i + 1]:
                i += 1
        else:
            # If not a duplicate, store the character
            s_list[k] = s_list[i]
            k += 1
        i += 1

    # Remove the remaining characters from the original string
    s_list = s_list[:k]

    # If any adjacent duplicates were removed, recursively check for more
    if k != n:
        s_list = remove_util(list(s_list), k)

    return s_list


def rremove(s):
    """
    Function to initiate the removal of adjacent duplicates.

    Args:
        s: Input string

    Returns:
        String with all adjacent duplicates removed
    """
    # Convert the string to a list to allow modification
    s_list = list(s)

    # Call the helper function
    return "".join(remove_util(s_list, len(s)))


def main():
    # Test Case 1
    s1 = "geeksforgeek"
    result1 = rremove(s1)
    print(f'Input: "{s1}"')
    print(f'Output: "{result1}"')
    print(f'Expected: "gksforgk"')
    print()

    # Test Case 2
    s2 = "abccbccba"
    result2 = rremove(s2)
    print(f'Input: "{s2}"')
    print(f'Output: "{result2}"')
    print(f'Expected: "" (empty string)')
    print()

    # Test Case 3 - No duplicates
    s3 = "abc"
    result3 = rremove(s3)
    print(f'Input: "{s3}"')
    print(f'Output: "{result3}"')
    print(f'Expected: "abc"')
    print()

    # Test Case 4 - All same characters
    s4 = "aaaa"
    result4 = rremove(s4)
    print(f'Input: "{s4}"')
    print(f'Output: "{result4}"')
    print(f'Expected: "" (empty string)')


if __name__ == "__main__":
    main()
