"""
Boggle - Find All Possible Words in a Board of Characters

Problem:
Given a dictionary of words and an m x n board of characters, find all words from
the dictionary that can be formed by a sequence of adjacent characters on the board.

Rules:
- Move in any of 8 directions (horizontal, vertical, diagonal)
- Each cell can be used only once per word

Algorithm: DFS with backtracking
- For each word in the dictionary, check if it can be formed on the board
- Start DFS from each cell that matches the first character
- Use backtracking to mark cells as visited during exploration

Time Complexity: O(N * M * L) where N = rows, M = cols, L = total characters in dictionary
Space Complexity: O(max_word_length) for recursion stack
"""


def find_words(board: list[list[str]], dictionary: list[str]) -> list[str]:
    """
    Find all dictionary words that can be formed on the board.

    Args:
        board: m x n grid of characters
        dictionary: List of words to search for

    Returns:
        List of words found on the board
    """
    if not board or not board[0] or not dictionary:
        return []

    rows, cols = len(board), len(board[0])
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def can_form_word(word: str, start_r: int, start_c: int) -> bool:
        """Check if a word can be formed starting from a given position."""
        if board[start_r][start_c] != word[0]:
            return False

        if len(word) == 1:
            return True

        # Use backtracking with board modification
        def dfs(idx: int, r: int, c: int) -> bool:
            if idx == len(word):
                return True

            # Temporarily mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[idx]:
                    if dfs(idx + 1, nr, nc):
                        board[r][c] = temp
                        return True

            # Restore the cell
            board[r][c] = temp
            return False

        return dfs(1, start_r, start_c)

    found_words = []

    for word in dictionary:
        if not word:
            continue

        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if can_form_word(word, r, c):
                    found_words.append(word)
                    found = True
                    break

    return found_words


def find_words_with_trie(board: list[list[str]], dictionary: list[str]) -> list[str]:
    """
    Find all dictionary words using a Trie for efficient prefix matching.

    Args:
        board: m x n grid of characters
        dictionary: List of words to search for

    Returns:
        List of words found on the board
    """
    if not board or not board[0] or not dictionary:
        return []

    # Build Trie from dictionary
    trie = {}
    for word in dictionary:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = word  # Mark end of word

    rows, cols = len(board), len(board[0])
    found_words = set()

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def dfs(r: int, c: int, node: dict) -> None:
        char = board[r][c]

        if char not in node or not isinstance(node[char], dict):
            return

        next_node = node[char]

        # Check if we found a word
        if "#" in next_node:
            found_words.add(next_node["#"])

        # Mark cell as visited
        board[r][c] = "#"

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                if board[nr][nc] in next_node and isinstance(
                    next_node[board[nr][nc]], dict
                ):
                    dfs(nr, nc, next_node)

        # Restore the cell
        board[r][c] = char

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie)

    return sorted(list(found_words))


if __name__ == "__main__":
    # Example 1
    board1 = [
        ["g", "e", "e"],
        ["k", "s", "k"],
        ["e", "e", "q"],
    ]
    dictionary1 = ["geeks", "quiz", "seek"]
    result1 = find_words([row[:] for row in board1], dictionary1)
    print(f"Example 1: {result1}")  # Output: ['geeks']

    # Example 2
    board2 = [
        ["g", "e", "e", "k"],
        ["k", "s", "e", "e"],
        ["q", "u", "i", "z"],
    ]
    dictionary2 = ["geeks", "quiz", "seek", "see"]
    result2 = find_words([row[:] for row in board2], dictionary2)
    print(f"Example 2: {result2}")

    # Example 3: Using Trie approach
    board3 = [
        ["g", "e", "e"],
        ["k", "s", "k"],
        ["e", "e", "q"],
    ]
    result3 = find_words_with_trie([row[:] for row in board3], dictionary2)
    print(f"Example 3 (Trie): {result3}")

    # Example 4
    board4 = [
        ["a", "b"],
        ["c", "d"],
    ]
    dictionary4 = ["abcd", "abdc", "acbd", "acdb", "abcd", "bdca"]
    result4 = find_words_with_trie([row[:] for row in board4], dictionary4)
    print(f"Example 4: {result4}")
