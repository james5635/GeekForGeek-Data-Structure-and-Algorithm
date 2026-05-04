"""
Longest Common Prefix using Word by Word Matching

Given an array of strings arr[], return the longest common prefix among
all strings. If there's no common prefix, return "".

This implementation uses the Trie-based approach for finding LCP.

Time Complexity: O(n * m) where n is number of strings, m is max string length
Space Complexity: O(n * m)
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.child_count = 0
        self.is_leaf = False


def insert(root, key):
    """Insert a key into the Trie."""
    curr = root
    for ch in key:
        idx = ord(ch) - ord("a")
        if curr.children[idx] is None:
            curr.children[idx] = TrieNode()
            curr.child_count += 1
        curr = curr.children[idx]
    curr.is_leaf = True


def walk_trie(root, s):
    """Walk the Trie to find the longest common prefix."""
    curr = root
    i = 0

    while curr.child_count == 1 and not curr.is_leaf:
        idx = ord(s[i]) - ord("a")
        i += 1
        curr = curr.children[idx]

    return s[:i]


def longest_common_prefix(arr):
    """
    Find the longest common prefix among all strings in the array.

    Args:
        arr: List of strings

    Returns:
        The longest common prefix string, or "" if none exists
    """
    if not arr:
        return ""

    root = TrieNode()

    for s in arr:
        insert(root, s)

    return walk_trie(root, arr[0])


if __name__ == "__main__":
    arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(f"arr = {arr1}")
    print(f"LCP: '{longest_common_prefix(arr1)}'")
    print()

    arr2 = ["apple", "ape", "april"]
    print(f"arr = {arr2}")
    print(f"LCP: '{longest_common_prefix(arr2)}'")
    print()

    arr3 = ["hello", "world"]
    print(f"arr = {arr3}")
    print(f"LCP: '{longest_common_prefix(arr3)}'")
