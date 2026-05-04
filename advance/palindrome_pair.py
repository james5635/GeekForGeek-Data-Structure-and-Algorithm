"""
Palindrome Pair in an Array of Words

Given an array of strings arr[] of size n, find if there exists two strings
arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome.

Uses Trie data structure to store all strings in reverse order and efficiently
search for palindromic pairs.

Time Complexity: O(n * k^2) where n is number of strings, k is max string length
Space Complexity: O(n * k)
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.indices = []
        self.idx = -1


def is_palindrome(word, i, j):
    """Check if substring word[i..j] is a palindrome."""
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def insert(root, word, idx):
    """Insert reverse of word into Trie, storing palindrome indices."""
    node = root

    for i in range(len(word) - 1, -1, -1):
        if is_palindrome(word, 0, i):
            node.indices.append(idx)

        index = ord(word[i]) - ord("a")
        if not node.children[index]:
            node.children[index] = TrieNode()

        node = node.children[index]

    node.idx = idx
    node.indices.append(idx)


def search(root, word, idx):
    """Search for a palindromic pair with the given word."""
    node = root
    for i in range(len(word)):
        index = ord(word[i]) - ord("a")

        if node.idx >= 0 and node.idx != idx and is_palindrome(word, i, len(word) - 1):
            return True

        if not node.children[index]:
            return False

        node = node.children[index]

    if node:
        for i in node.indices:
            if idx != i:
                return True

    return False


def palindrome_pair(arr):
    """
    Check if there exists a palindrome pair in the array.

    Args:
        arr: List of strings

    Returns:
        True if a palindrome pair exists, False otherwise
    """
    root = TrieNode()

    for i in range(len(arr)):
        insert(root, arr[i], i)

    for i in range(len(arr)):
        if search(root, arr[i], i):
            return True

    return False


if __name__ == "__main__":
    arr1 = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
    print(f"arr = {arr1}")
    print(f"Palindrome pair exists: {palindrome_pair(arr1)}")
    print()

    arr2 = ["abc", "xyxcba", "geekst", "or", "keeg", "bc"]
    print(f"arr = {arr2}")
    print(f"Palindrome pair exists: {palindrome_pair(arr2)}")
    print()

    arr3 = ["abc", "ab", "xyz"]
    print(f"arr = {arr3}")
    print(f"Palindrome pair exists: {palindrome_pair(arr3)}")
