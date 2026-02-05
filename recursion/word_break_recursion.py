"""
Word Break Problem
https://www.geeksforgeeks.org/dsa/word-break-problem-dp-32/

Given a string s and a dictionary of words, check if s can be segmented into a sequence of valid words.

Approach: Top-Down DP (Memoization) - O(n^2) Time and O(n+m) Space
"""


def word_break_rec(ind, s, dictionary, dp):
    """
    Recursive function with memoization to check if string can be segmented.

    Args:
        ind: Current index in the string
        s: The input string
        dictionary: Set of valid words
        dp: Memoization array

    Returns:
        True if the substring starting at ind can be segmented
    """
    if ind >= len(s):
        return True

    if dp[ind] != -1:
        return dp[ind] == 1

    possible = False

    for temp in dictionary:
        if len(temp) > len(s) - ind:
            continue

        # Check if substring matches
        if s[ind : ind + len(temp)] == temp:
            possible |= word_break_rec(ind + len(temp), s, dictionary, dp)

    dp[ind] = 1 if possible else 0
    return possible


def word_break(s, dictionary):
    """
    Check if string s can be segmented using words from dictionary.

    Args:
        s: The input string
        dictionary: List/Set of valid words

    Returns:
        True if string can be segmented, False otherwise
    """
    n = len(s)
    dp = [-1] * (n + 1)
    # Convert dictionary to set for O(1) lookup
    dict_set = set(dictionary)
    return word_break_rec(0, s, dict_set, dp)


def main():
    """
    Main function to demonstrate the algorithm.
    """
    # Test case 1
    print("Test Case 1:")
    s = "ilike"
    dictionary = {"i", "like", "gfg"}
    print(f'String: "{s}"')
    print(f"Dictionary: {dictionary}")
    print(f"Output: {'true' if word_break(s, dictionary) else 'false'}")
    print()

    # Test case 2
    print("Test Case 2:")
    s = "ilikegfg"
    dictionary = {"i", "like", "man", "india", "gfg"}
    print(f'String: "{s}"')
    print(f"Dictionary: {dictionary}")
    print(f"Output: {'true' if word_break(s, dictionary) else 'false'}")
    print()

    # Test case 3
    print("Test Case 3:")
    s = "ilikemangoes"
    dictionary = {"i", "like", "gfg"}
    print(f'String: "{s}"')
    print(f"Dictionary: {dictionary}")
    print(f"Output: {'true' if word_break(s, dictionary) else 'false'}")
    print()

    # Test case 4
    print("Test Case 4:")
    s = "leetcode"
    dictionary = {"leet", "code"}
    print(f'String: "{s}"')
    print(f"Dictionary: {dictionary}")
    print(f"Output: {'true' if word_break(s, dictionary) else 'false'}")


if __name__ == "__main__":
    main()
