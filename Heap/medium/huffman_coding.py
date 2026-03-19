"""
Huffman Coding - GeeksforGeeks
https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

Problem: Huffman coding is a lossless data compression algorithm. Assign variable-length
codes to input characters based on their frequencies. Codes are prefix codes (no code
is a prefix of another).

Algorithm:
1. Create a leaf node for each character and build a min heap
2. Extract two nodes with minimum frequency
3. Create a new internal node with frequency = sum of the two nodes
4. Make extracted nodes as left and right child
5. Add new node to min heap
6. Repeat until heap has only one node

Time Complexity: O(n*log(n))
Space Complexity: O(n)
"""

import heapq


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.data < other.data


def preorder(root, ans, curr):
    """
    Traverse tree in preorder and collect Huffman codes.
    Moving left adds '0', moving right adds '1'.
    """
    if root is None:
        return

    if root.left is None and root.right is None:
        ans.append(curr)
        return

    preorder(root.left, ans, curr + "0")
    preorder(root.right, ans, curr + "1")


def huffman_codes(s, freq):
    """
    Generate Huffman codes for characters in string s with given frequencies.

    Args:
        s: Input string
        freq: List of frequencies for each character in s

    Returns:
        List of Huffman codes for each character
    """
    n = len(s)

    pq = []
    for i in range(n):
        tmp = Node(freq[i])
        heapq.heappush(pq, tmp)

    while len(pq) >= 2:
        l = heapq.heappop(pq)
        r = heapq.heappop(pq)

        new_node = Node(l.data + r.data)
        new_node.left = l
        new_node.right = r

        heapq.heappush(pq, new_node)

    root = heapq.heappop(pq)
    ans = []
    preorder(root, ans, "")
    return ans


def huffman_codes_with_mapping(s, freq):
    """
    Generate Huffman codes with character-to-code mapping.

    Returns:
        Tuple of (codes list, code mapping dictionary)
    """
    n = len(s)

    pq = []
    for i in range(n):
        tmp = Node(freq[i])
        heapq.heappush(pq, tmp)

    while len(pq) >= 2:
        l = heapq.heappop(pq)
        r = heapq.heappop(pq)

        new_node = Node(l.data + r.data)
        new_node.left = l
        new_node.right = r

        heapq.heappush(pq, new_node)

    root = heapq.heappop(pq)
    ans = []
    code_map = {}

    def get_codes(node, curr):
        if node is None:
            return
        if node.left is None and node.right is None:
            ans.append(curr)
            code_map[node.data] = curr
            return
        get_codes(node.left, curr + "0")
        get_codes(node.right, curr + "1")

    get_codes(root, "")
    return ans, code_map


if __name__ == "__main__":
    s = "abcdef"
    freq = [5, 9, 12, 13, 16, 45]

    codes = huffman_codes(s, freq)
    print("Huffman codes:", codes)
    # Output: codes for f, c, d, a, b, e

    codes_list, code_map = huffman_codes_with_mapping(s, freq)
    print("\nCode mapping:")
    for i, char in enumerate(s):
        print(f"  {char}: {code_map[freq[i]]}")

    # Encode a message
    message = "abac"
    encoded = "".join(code_map[freq[s.index(c)]] for c in message)
    print(f"\nOriginal: {message}")
    print(f"Encoded: {encoded}")
