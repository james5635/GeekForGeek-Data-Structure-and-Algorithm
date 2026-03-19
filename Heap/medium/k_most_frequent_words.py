"""
K Most Frequent Words from a File - GeeksforGeeks
https://www.geeksforgeeks.org/dsa/find-the-k-most-frequent-words-from-a-file/

Problem: Given a book of words and an integer K, find the top K most frequent words.
Design a dynamic data structure that can handle new words being added.

Approaches:
1. Hash Map + Counter (simple, uses built-in)
2. Hash Map + Min Heap (efficient for streaming)
3. Trie + Min Heap (for memory-efficient large datasets)

Time Complexity: O(n + n*log(k)) = O(n*log(k)) for heap approach
Space Complexity: O(n) for storing words
"""

from collections import Counter, defaultdict
import heapq


def process_text_simple(text, k):
    """
    Simple approach using Counter.most_common()
    O(n) time, O(n) space
    """
    freq_map = Counter(text.split())
    res = freq_map.most_common(k)
    return res


def process_text_heap(text, k):
    """
    Use min-heap of size k to track top k frequent words.
    O(n*log(k)) time, O(n) space
    """
    freq_map = Counter(text.split())

    pq = []
    for word, freq in freq_map.items():
        heapq.heappush(pq, (freq, word))
        if len(pq) > k:
            heapq.heappop(pq)

    res = []
    while pq:
        freq, word = heapq.heappop(pq)
        res.append((word, freq))

    res.reverse()
    return res


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.freq = 0
        self.ind = -1
        self.child = [None] * 26


class MinHeapNode:
    def __init__(self):
        self.root = None
        self.freq = 0
        self.word = ""


class MinHeap:
    def __init__(self, cap):
        self.cap = cap
        self.count = 0
        self.arr = [MinHeapNode() for _ in range(cap)]

    def swap_nodes(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]
        self.arr[a].root.ind = a
        self.arr[b].root.ind = b

    def heapify(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        mini = idx
        if left < self.count and self.arr[left].freq < self.arr[mini].freq:
            mini = left
        if right < self.count and self.arr[right].freq < self.arr[mini].freq:
            mini = right
        if mini != idx:
            self.swap_nodes(idx, mini)
            self.heapify(mini)

    def build(self):
        for i in range((self.count - 1) // 2, -1, -1):
            self.heapify(i)


def insert_trie(mH, root, word):
    if root.ind != -1:
        mH.arr[root.ind].freq += 1
        mH.heapify(root.ind)
    elif mH.count < mH.cap:
        node = MinHeapNode()
        node.root = root
        node.freq = root.freq
        node.word = word
        mH.arr[mH.count] = node
        root.ind = mH.count
        mH.count += 1
        mH.build()
    elif root.freq > mH.arr[0].freq:
        mH.arr[0].root.ind = -1
        node = MinHeapNode()
        node.root = root
        node.freq = root.freq
        node.word = word
        mH.arr[0] = node
        root.ind = 0
        mH.heapify(0)


def insert_util(root, mH, word, index=0):
    if root is None:
        root = TrieNode()
    if index < len(word):
        pos = ord(word[index].lower()) - ord("a")
        if 0 <= pos < 26:
            if root.child[pos] is None:
                root.child[pos] = TrieNode()
            insert_util(root.child[pos], mH, word, index + 1)
    else:
        if root.is_end:
            root.freq += 1
        else:
            root.is_end = True
            root.freq = 1
        insert_trie(mH, root, word)


def process_text_trie(text, k):
    """
    Use Trie + Min Heap for memory-efficient implementation.
    Good for large datasets with many unique words.
    """
    mH = MinHeap(k)
    root = TrieNode()

    for word in text.split():
        insert_util(root, mH, word)

    return [(mH.arr[i].word, mH.arr[i].freq) for i in range(mH.count)]


if __name__ == "__main__":
    text = (
        "Welcome to the world of Geeks Geeks for Geeks is great "
        "and well written well thought and well explained"
    )
    k = 5

    print("Text:", text[:50], "...")
    print(f"\nTop {k} frequent words:")

    print("\n1. Simple (Counter):")
    for word, freq in process_text_simple(text, k):
        print(f"   {word}: {freq}")

    print("\n2. Heap approach:")
    for word, freq in process_text_heap(text, k):
        print(f"   {word}: {freq}")

    print("\n3. Trie + Heap approach:")
    for word, freq in process_text_trie(text, k):
        print(f"   {word}: {freq}")
