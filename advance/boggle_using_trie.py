"""
Boggle using Trie

Given a dictionary and a M x N board where every cell has one character,
find all possible words that can be formed by a sequence of adjacent characters.
We can move to any of 8 adjacent characters, but a word should not have multiple
instances of the same cell.

Time Complexity: O(W * L + B * 8^L) where W is number of words, L is max word length,
                 B is total board cells (N^2)
Space Complexity: O(W * L + B)
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


def _char_to_index(ch):
    return ord(ch.upper()) - ord("A")


def insert(root, key):
    """Insert a word into the Trie."""
    pCrawl = root
    for ch in key:
        index = _char_to_index(ch)
        if not pCrawl.children[index]:
            pCrawl.children[index] = TrieNode()
        pCrawl = pCrawl.children[index]
    pCrawl.isEndOfWord = True


def is_safe(i, j, rows, cols, visited):
    """Check if the current cell is within bounds and not visited."""
    return 0 <= i < rows and 0 <= j < cols and not visited[i][j]


def search_word(root, boggle, i, j, rows, cols, visited, string, found_words):
    """Recursively search for words starting from position (i, j)."""
    if root.isEndOfWord:
        found_words.add(string)

    if is_safe(i, j, rows, cols, visited):
        visited[i][j] = True

        for k in range(26):
            if root.children[k] is not None:
                ch = chr(k + ord("A"))

                directions = [
                    (i + 1, j + 1),
                    (i, j + 1),
                    (i - 1, j + 1),
                    (i + 1, j),
                    (i + 1, j - 1),
                    (i, j - 1),
                    (i - 1, j - 1),
                    (i - 1, j),
                ]

                for ni, nj in directions:
                    if is_safe(ni, nj, rows, cols, visited) and boggle[ni][nj] == ch:
                        search_word(
                            root.children[k],
                            boggle,
                            ni,
                            nj,
                            rows,
                            cols,
                            visited,
                            string + ch,
                            found_words,
                        )

        visited[i][j] = False


def find_words(boggle, root):
    """Find all words from the dictionary that can be formed on the boggle board."""
    rows = len(boggle)
    cols = len(boggle[0])
    found_words = set()

    for i in range(rows):
        for j in range(cols):
            index = _char_to_index(boggle[i][j])
            if root.children[index]:
                visited = [[False] * cols for _ in range(rows)]
                search_word(
                    root.children[index],
                    boggle,
                    i,
                    j,
                    rows,
                    cols,
                    visited,
                    boggle[i][j],
                    found_words,
                )

    return sorted(list(found_words))


if __name__ == "__main__":
    dictionary = ["GEEKS", "FOR", "QUIZ", "GEE"]

    root = TrieNode()
    for word in dictionary:
        insert(root, word)

    boggle = [["G", "I", "Z"], ["U", "E", "K"], ["Q", "S", "E"]]

    found = find_words(boggle, root)
    print("Words found in boggle:")
    for word in found:
        print(f"  {word}")

    print()

    boggle2 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary2 = ["GEEKS", "ABCFIHGDE"]
    root2 = TrieNode()
    for word in dictionary2:
        insert(root2, word)

    found2 = find_words(boggle2, root2)
    print("Words found in second boggle:")
    for word in found2:
        print(f"  {word}")
