"""
Check if Strings Can Be Made Equal by Inserting at Most One Character

Approach:
1. If strings are equal, return Yes (0 insertions needed)
2. If lengths differ by more than 1, return No (would need >1 insertion)
3. Use two pointers to find first mismatch
4. Try skipping one character from longer string and check if rest matches
5. If mismatch in equal-length strings, skip from either and compare

Time Complexity: O(n)
Space Complexity: O(1)
"""


def can_be_equal_by_one_insert(s1, s2):
    """
    Check if s1 can be made equal to s2 by inserting at most 1 character into s1.
    Returns True if strings can be equal with at most one insertion.
    """
    if s1 == s2:
        return True

    len1, len2 = len(s1), len(s2)

    if abs(len1 - len2) > 1:
        return False

    if len1 == len2:
        return can_equal_by_one_insert_same_length(s1, s2)
    elif len1 > len2:
        return can_equal_by_one_insert_longer(s1, s2)
    else:
        return can_equal_by_one_insert_longer(s2, s1)


def can_equal_by_one_insert_same_length(s1, s2):
    """
    Both strings same length - can we make them equal by one insertion?
    This means there should be exactly one mismatch.
    """
    mismatch_count = 0
    mismatch_idx = -1

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatch_count += 1
            mismatch_idx = i
            if mismatch_count > 1:
                return False

    return mismatch_count == 1


def can_equal_by_one_insert_longer(longer, shorter):
    """
    Check if we can make longer equal to shorter by inserting one char
    into the shorter string at the right position.
    """
    i = j = 0
    inserted = False

    while i < len(longer) and j < len(shorter):
        if longer[i] == shorter[j]:
            i += 1
            j += 1
        else:
            if inserted:
                return False
            inserted = True
            i += 1

    return True


def can_be_equal_v2(s1, s2):
    """
    Alternative approach using deque for simulation.
    Check if strings differ by at most 1 character.
    """
    from collections import deque

    if s1 == s2:
        return True

    len1, len2 = len(s1), len(s2)
    if abs(len1 - len2) > 1:
        return False

    if len1 == len2:
        diff_count = sum(1 for a, b in zip(s1, s2) if a != b)
        return diff_count == 1

    if len1 > len2:
        longer, shorter = s1, s2
    else:
        longer, shorter = s2, s1

    dq_long = deque(longer)
    dq_short = deque(shorter)

    i = j = 0
    inserted = False

    while i < len(longer) and j < len(shorter):
        if longer[i] == shorter[j]:
            i += 1
            j += 1
        else:
            if inserted:
                return False
            inserted = True
            i += 1

    return True


def main():
    print("=== Check if Strings Can Be Made Equal by Inserting at Most 1 ===\n")

    test_cases = [
        ("geeksforgeeks", "geeksgeeks", "No"),
        ("geekforgeeks", "geeksgeeks", "No"),
        ("abc", "abc", "Yes"),
        ("abc", "ab", "Yes"),
        ("ab", "abc", "Yes"),
        ("abcd", "ab", "No"),
        ("abc", "def", "No"),
        ("a", "ab", "Yes"),
        ("ab", "a", "Yes"),
        ("abc", "axc", "Yes"),
        ("abc", "abd", "Yes"),
        ("abc", "axbc", "Yes"),
    ]

    for s1, s2, expected in test_cases:
        result = can_be_equal_by_one_insert(s1, s2)
        output = "Yes" if result else "No"
        status = "PASS" if output == expected else "FAIL"
        print(f"Input: '{s1}', '{s2}'")
        print(f"Output: {output}")
        print(f"Expected: {expected}")
        print(f"Status: {status}\n")


if __name__ == "__main__":
    main()
