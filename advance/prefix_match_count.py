"""
Count of Strings Whose Prefix Match with the Given String to a Given Length k

Given an array of strings arr[] and some queries where each query consists of
a string str and an integer k. The task is to find the count of strings in arr[]
whose prefix of length k matches with the k length prefix of str.

Time Complexity: O(n * L + k) where n is number of strings, L is max string length
Space Complexity: O(n * L)
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.freq = 0


def insert(s, root):
    """Insert a string into the Trie, incrementing frequency at each node."""
    cur = root
    for ch in s:
        idx = ord(ch) - ord("a")
        if cur.children[idx] is None:
            cur.children[idx] = TrieNode()
        cur.children[idx].freq += 1
        cur = cur.children[idx]
    return root


def prefix_match_count(arr, k, string):
    """
    Count strings whose prefix of length k matches with the k length prefix of string.

    Args:
        arr: List of strings to search in
        k: Length of prefix to match
        string: Query string

    Returns:
        Count of matching strings
    """
    root = TrieNode()

    for s in arr:
        insert(s, root)

    count = 0
    cur = root

    for ch in string:
        idx = ord(ch) - ord("a")
        if cur.children[idx] is None:
            return 0
        cur = cur.children[idx]
        count += 1
        if count == k:
            return cur.freq

    return 0


if __name__ == "__main__":
    arr = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]

    result1 = prefix_match_count(arr, 3, "abbg")
    print(f"Query: str='abbg', k=3 => Count: {result1}")

    arr2 = ["geeks", "geeksforgeeks", "forgeeks"]
    result2 = prefix_match_count(arr2, 2, "geeks")
    print(f"Query: str='geeks', k=2 => Count: {result2}")

    result3 = prefix_match_count(arr, 1, "a")
    print(f"Query: str='a', k=1 => Count: {result3}")
