"""
Trie Delete

Delete a key from Trie. The following are possible conditions when deleting:
1. Key may not be there in trie - Delete operation should not modify trie.
2. Key present as unique key - Delete all the nodes.
3. Key is prefix key of another long key - Unmark the leaf node.
4. Key present having at least one other key as prefix - Delete nodes from end
   until first leaf node of longest prefix key.

Time Complexity: O(n) where n is the key length
Space Complexity: O(n * m) where n is max word length and m is total words
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


def get_node():
    """Create and return a new TrieNode."""
    return TrieNode()


def insert(root, key):
    """Insert a key into the Trie."""
    pCrawl = root
    for ch in key:
        index = ord(ch) - ord("a")
        if not pCrawl.children[index]:
            pCrawl.children[index] = get_node()
        pCrawl = pCrawl.children[index]
    pCrawl.isEndOfWord = True


def search(root, key):
    """Search for a key in the Trie. Returns True if found."""
    pCrawl = root
    for ch in key:
        index = ord(ch) - ord("a")
        if not pCrawl.children[index]:
            return False
        pCrawl = pCrawl.children[index]
    return pCrawl is not None and pCrawl.isEndOfWord


def is_empty(root):
    """Check if the node has no children."""
    for i in range(26):
        if root.children[i]:
            return False
    return True


def remove(root, key, depth=0):
    """Recursively delete a key from the Trie."""
    if not root:
        return None

    if depth == len(key):
        if root.isEndOfWord:
            root.isEndOfWord = False
        if is_empty(root):
            root = None
        return root

    index = ord(key[depth]) - ord("a")
    root.children[index] = remove(root.children[index], key, depth + 1)

    if is_empty(root) and not root.isEndOfWord:
        root = None

    return root


if __name__ == "__main__":
    keys = [
        "the",
        "a",
        "there",
        "answer",
        "any",
        "by",
        "bye",
        "their",
        "hero",
        "heroplane",
    ]
    root = get_node()

    for key in keys:
        insert(root, key)

    print("Search before deletion:")
    print(f"  'the': {search(root, 'the')}")
    print(f"  'these': {search(root, 'these')}")
    print(f"  'hero': {search(root, 'hero')}")
    print(f"  'heroplane': {search(root, 'heroplane')}")

    print("\nDeleting 'heroplane'...")
    root = remove(root, "heroplane")

    print("\nSearch after deletion:")
    print(f"  'the': {search(root, 'the')}")
    print(f"  'these': {search(root, 'these')}")
    print(f"  'hero': {search(root, 'hero')}")
    print(f"  'heroplane': {search(root, 'heroplane')}")

    print("\nDeleting 'the' (prefix of 'there' and 'their')...")
    root = remove(root, "the")

    print("\nSearch after deleting 'the':")
    print(f"  'the': {search(root, 'the')}")
    print(f"  'there': {search(root, 'there')}")
    print(f"  'their': {search(root, 'their')}")
