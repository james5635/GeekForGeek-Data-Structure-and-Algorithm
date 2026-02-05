"""
Length of Longest Palindromic Substring using Recursion

Given a string S, find the length of the longest substring which is a palindrome.

Examples:
- S = "aaaabbaa" -> Output: 6 (substring "aabbaa")
- S = "banana" -> Output: 5 (substring "anana")

Approach:
Using recursion to break the problem into smaller sub-problems:
1. Compare start and end characters of the string
2. If they are equal, recursively call for substring excluding corner characters
3. If not equal, recursively try excluding start or end character one at a time
4. Track the count of palindromic characters matched

Base Cases:
- If i > j: return count
- If i == j: return count + 1 (single character is always palindrome)

Time Complexity: O(2^n) in worst case
Auxiliary Space: O(n) due to recursion stack
"""


def longest_palindromic(s, i, j, count):
    """
    Find the length of longest palindromic substring using recursion.

    Args:
        s: Input string
        i: Start index
        j: End index
        count: Current count of palindrome length

    Returns:
        int: Length of longest palindromic substring
    """
    # Base condition when start index is greater than end index
    if i > j:
        return count

    # Base condition when both start and end index are equal
    if i == j:
        return count + 1

    # Condition when corner characters are equal
    if s[i] == s[j]:
        # Recursive call to find the longest Palindromic string
        # by excluding the corner characters
        count = longest_palindromic(s, i + 1, j - 1, count + 2)
        return max(
            count,
            max(
                longest_palindromic(s, i + 1, j, 0), longest_palindromic(s, i, j - 1, 0)
            ),
        )

    # Recursive call to find the longest Palindromic string
    # by including one corner character at a time
    return max(longest_palindromic(s, i + 1, j, 0), longest_palindromic(s, i, j - 1, 0))


def find_longest_palindrome(s):
    """
    Wrapper function to find longest palindromic substring length.

    Args:
        s: Input string

    Returns:
        int: Length of longest palindromic substring
    """
    n = len(s)
    if n == 0:
        return 0
    return longest_palindromic(s, 0, n - 1, 0)


def main():
    # Test Case 1
    s1 = "aaaabbaa"
    result1 = find_longest_palindrome(s1)
    print(f'String: "{s1}"')
    print(f"Longest Palindromic Substring Length: {result1}")
    print(f"Expected: 6")
    print(f'Longest Palindrome: "aabbaa"')
    print()

    # Test Case 2
    s2 = "banana"
    result2 = find_longest_palindrome(s2)
    print(f'String: "{s2}"')
    print(f"Longest Palindromic Substring Length: {result2}")
    print(f"Expected: 5")
    print(f'Longest Palindrome: "anana"')
    print()

    # Test Case 3 - Single character
    s3 = "a"
    result3 = find_longest_palindrome(s3)
    print(f'String: "{s3}"')
    print(f"Longest Palindromic Substring Length: {result3}")
    print(f"Expected: 1")
    print()

    # Test Case 4 - All same characters
    s4 = "aaaa"
    result4 = find_longest_palindrome(s4)
    print(f'String: "{s4}"')
    print(f"Longest Palindromic Substring Length: {result4}")
    print(f"Expected: 4")
    print()

    # Test Case 5 - No palindrome longer than 1
    s5 = "abcd"
    result5 = find_longest_palindrome(s5)
    print(f'String: "{s5}"')
    print(f"Longest Palindromic Substring Length: {result5}")
    print(f"Expected: 1")


if __name__ == "__main__":
    main()
