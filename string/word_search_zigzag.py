"""
Word Search with Zigzag Movement Allowed

Given a 2D grid of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where "adjacent" cells are those which are horizontally, vertically, or
diagonally neighboring (8 directions total). This is the "zigzag" movement.

The same letter cell may not be used more than once.

Examples:
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
- word = "ABFSED" -> True (can move diagonally)
- word = "ABFD" -> True

Time Complexity: O(m * n * 8^L) where L is the length of the word
Space Complexity: O(L) for recursion stack
"""


def existZigzag(board, word):
    """
    Check if word exists with zigzag (8-directional) movement allowed
    """
    if not board or not board[0]:
        return False

    m, n = len(board), len(board[0])

    # All 8 directions: up, down, left, right, and 4 diagonals
    directions = [
        (-1, 0),  # Up
        (1, 0),  # Down
        (0, -1),  # Left
        (0, 1),  # Right
        (-1, -1),  # Up-Left
        (-1, 1),  # Up-Right
        (1, -1),  # Down-Left
        (1, 1),  # Down-Right
    ]

    def dfs(i, j, k):
        """
        DFS to search for word starting from position (i, j)
        """
        if k == len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False

        # Mark as visited
        temp = board[i][j]
        board[i][j] = "#"

        # Try all 8 directions
        found = False
        for di, dj in directions:
            if dfs(i + di, j + dj, k + 1):
                found = True
                break

        # Restore
        board[i][j] = temp
        return found

    # Try starting from each cell
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True

    return False


def existZigzagWithPath(board, word):
    """
    Return the path taken if word exists
    """
    if not board or not board[0]:
        return []

    m, n = len(board), len(board[0])
    path = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(i, j, k):
        if k == len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = "#"
        path.append((i, j, temp))

        for di, dj in directions:
            if dfs(i + di, j + dj, k + 1):
                return True

        path.pop()
        board[i][j] = temp
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return path

    return []


def findAllWordsZigzag(board, words):
    """
    Find all words that can be formed with zigzag movement
    """
    return [word for word in words if existZigzag(board, word)]


# Test the function
if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    test_words = [
        "ABFSED",  # Diagonal movement
        "ABFD",  # Diagonal then down
        "ASF",  # Down then diagonal
        "ACEFD",  # Diagonal path
        "ABC",  # Regular horizontal
        "ABCB",  # Should fail - reuse not allowed
    ]

    print("Word Search with Zigzag Movement (8 directions)")
    print("=" * 50)
    print("Board:")
    for row in board:
        print("  " + str(row))
    print()

    for word in test_words:
        result = existZigzag(board, word)
        print(f"Word '{word}': {result}")

        if result:
            path = existZigzagWithPath(board, word)
            path_str = " -> ".join([f"({r},{c})={ch}" for r, c, ch in path])
            print(f"  Path: {path_str}")
        print()

    print("\nComparison with standard word search:")
    print("- Standard: 4 directions (up, down, left, right)")
    print("- Zigzag: 8 directions (adds 4 diagonals)")
    print("- Zigzag allows more paths, making it easier to find words")
