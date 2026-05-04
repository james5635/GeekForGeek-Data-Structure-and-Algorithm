"""
Trie Insert and Search

The Trie data structure is used to store a set of keys represented as strings.
It allows for efficient retrieval and storage of keys, making it highly effective
in handling large datasets.

Operations:
- Insert: O(n) Time, O(n) Space where n is the length of the word
- Search: O(n) Time, O(1) Space where n is the length of the word
- Prefix Search: O(n) Time, O(1) Space where n is the length of the prefix
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        """Insert a key into the Trie."""
        curr = self.root
        for c in key:
            index = ord(c) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, key):
        """Search for a complete key in the Trie. Returns True if found."""
        curr = self.root
        for c in key:
            index = ord(c) - ord("a")
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isLeaf

    def is_prefix(self, prefix):
        """Check if a prefix exists in the Trie."""
        curr = self.root
        for c in prefix:
            index = ord(c) - ord("a")
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True


if __name__ == "__main__":
    trie = Trie()
    arr = ["and", "ant", "do", "dad"]
    for s in arr:
        trie.insert(s)

    search_keys = ["do", "gee", "bat"]
    print("Search results:")
    for s in search_keys:
        print(f"  {s}: {trie.search(s)}")

    prefix_keys = ["ge", "ba", "do", "de"]
    print("\nPrefix search results:")
    for s in prefix_keys:
        print(f"  {s}: {trie.is_prefix(s)}")
