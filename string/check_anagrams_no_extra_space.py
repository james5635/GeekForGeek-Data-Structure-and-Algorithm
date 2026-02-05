"""
Check if Two Strings are Anagrams without Using Extra Space

Given two strings, check if they are anagrams of each other without using
any extra space (i.e., O(1) space complexity).

Anagram: Two strings are anagrams if they contain the same characters
with the same frequencies.

Examples:
- "listen", "silent" -> True
- "hello", "world" -> False

Note: This problem is challenging because typically we use a hash map
or array (256 chars) which is O(1) space but technically uses extra space.

The strict O(1) space approach requires sorting the strings in-place.

Time Complexity: O(n log n) for sorting approach
Space Complexity: O(1) or O(n) depending on implementation
"""


def areAnagramsSort(s1, s2):
    """
    Check if strings are anagrams by sorting (in-place modification)
    This uses O(1) extra space if we sort in place, but strings are immutable in Python.
    So we convert to lists which technically uses O(n) space.
    """
    if len(s1) != len(s2):
        return False

    # Convert to lists for in-place sorting
    # In Python, strings are immutable, so we need lists
    # This technically uses O(n) space due to list creation
    list1 = list(s1)
    list2 = list(s2)

    # Sort both lists
    list1.sort()
    list2.sort()

    # Compare sorted lists
    return list1 == list2


def areAnagramsBitwise(s1, s2):
    """
    Using XOR operations for limited character sets
    This only works if strings have no duplicates and same length
    """
    if len(s1) != len(s2):
        return False

    xor_result = 0
    sum1, sum2 = 0, 0

    for i in range(len(s1)):
        xor_result ^= ord(s1[i]) ^ ord(s2[i])
        sum1 += ord(s1[i])
        sum2 += ord(s2[i])

    # XOR should be 0 and sums should be equal
    return xor_result == 0 and sum1 == sum2


def areAnagramsArray(s1, s2):
    """
    Standard approach using count array
    Uses O(1) space for fixed character set (26 for lowercase letters)
    or O(256) for ASCII which is technically constant.
    """
    if len(s1) != len(s2):
        return False

    # For lowercase letters only
    count = [0] * 26

    for i in range(len(s1)):
        count[ord(s1[i]) - ord("a")] += 1
        count[ord(s2[i]) - ord("a")] -= 1

    # Check if all counts are zero
    for c in count:
        if c != 0:
            return False

    return True


def areAnagramsInPlace(s1, s2):
    """
    Attempt at truly O(1) space by modifying one of the strings
    Note: In Python, strings are immutable, so this is just conceptual
    """
    if len(s1) != len(s2):
        return False

    # Use one string as a "frequency map" by marking characters
    # This is a conceptual implementation
    s2_list = list(s2)

    for char in s1:
        found = False
        for i in range(len(s2_list)):
            if s2_list[i] == char:
                s2_list[i] = None  # Mark as used
                found = True
                break
        if not found:
            return False

    return True


# Test the functions
if __name__ == "__main__":
    test_cases = [
        ("listen", "silent"),
        ("hello", "world"),
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("aabbcc", "abcabc"),
        ("abc", "abcd"),
    ]

    print("Check Anagrams Without Extra Space")
    print("=" * 50)

    for s1, s2 in test_cases:
        result_sort = areAnagramsSort(s1, s2)
        result_array = areAnagramsArray(s1, s2)
        result_inplace = areAnagramsInPlace(s1, s2)

        print(f"String 1: '{s1}'")
        print(f"String 2: '{s2}'")
        print(f"  Sort approach: {result_sort}")
        print(f"  Array approach: {result_array}")
        print(f"  In-place approach: {result_inplace}")
        print()

    print("Note: True O(1) space is difficult in Python due to")
    print("string immutability. Sorting approach would be O(1)")
    print("in languages with mutable strings (like C/C++).")
