"""
Counting Common Prefix/Suffix Strings in Two Lists

Given two lists of strings s1 and s2, count the number of strings in s2
which are either a suffix or prefix of at least one string in s1.

Time Complexity: O(n^2) where n is total number of strings
Space Complexity: O(1)
"""


def prefix_suffix_string(s1, s2):
    """
    Count strings in s2 that are prefix or suffix of any string in s1.

    Args:
        s1: First list of strings
        s2: Second list of strings to check

    Returns:
        Count of strings in s2 that are prefix or suffix of some string in s1
    """
    count = 0
    for s in s2:
        for t in s1:
            if t.startswith(s) or t.endswith(s):
                count += 1
                break
    return count


if __name__ == "__main__":
    s1 = ["cat", "catanddog", "lion"]
    s2 = ["cat", "dog", "rat"]
    result = prefix_suffix_string(s1, s2)
    print(f"s1 = {s1}")
    print(f"s2 = {s2}")
    print(f"Count: {result}")
    print()

    s1_2 = ["jrjiml", "tchetn", "ucrhye", "ynayhy", "cuhffd", "cvgpoiu", "znyadv"]
    s2_2 = ["jr", "ml", "cvgpoi", "gpoiu", "wnmkmluc", "geheqe", "uglxagyl", "uyxdroj"]
    result2 = prefix_suffix_string(s1_2, s2_2)
    print(f"s1 = {s1_2}")
    print(f"s2 = {s2_2}")
    print(f"Count: {result2}")
