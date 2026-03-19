def can_be_made_equal(s1, s2):
    n1, n2 = len(s1), len(s2)

    prefix = 0
    while prefix < n1 and prefix < n2 and s1[prefix] == s2[prefix]:
        prefix += 1

    suffix = 0
    while (
        suffix < n1 - prefix
        and suffix < n2 - prefix
        and s1[n1 - 1 - suffix] == s2[n2 - 1 - suffix]
    ):
        suffix += 1

    return prefix + suffix >= min(n1, n2) and min(n1, n2) > 0


if __name__ == "__main__":
    assert can_be_made_equal("geeksforgeeks", "geeksgeeks") == True
    assert can_be_made_equal("abc", "abc") == True
    assert can_be_made_equal("abc", "def") == False
    assert can_be_made_equal("abc", "abdc") == True
    assert can_be_made_equal("abc", "abcd") == True
    assert can_be_made_equal("abc", "dabc") == True
    assert can_be_made_equal("", "") == False
    assert can_be_made_equal("a", "b") == False
    assert can_be_made_equal("a", "") == False
    assert can_be_made_equal("ab", "ba") == False
    assert can_be_made_equal("hello", "helllo") == True

    print("All tests passed")
