"""
Word Search

Given an m x n grid of characters board and a string word, return true if
word exists in the grid. The word can be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Examples:
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
- word = "ABCCED" -> True
- word = "SEE" -> True
- word = "ABCB" -> False

Time Complexity: O(m * n * 4^L) where L is the length of the word
Space Complexity: O(L) for recursion stack
"""


def exist(board, word):
    """
    Check if word exists in the board using DFS
    """
    if not board or not board[0]:
        return False

    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        """
        DFS to search for word starting from position (i, j)
        k is the current index in word we're looking for
        """
        # Base case: if we've found all characters
        if k == len(word):
            return True

        # Check bounds and if current cell matches
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False

        # Mark current cell as visited
        temp = board[i][j]
        board[i][j] = "#"  # Use a special marker

        # Explore all 4 directions
        found = (
            dfs(i + 1, j, k + 1)  # Down
            or dfs(i - 1, j, k + 1)  # Up
            or dfs(i, j + 1, k + 1)  # Right
            or dfs(i, j - 1, k + 1)
        )  # Left

        # Restore the cell
        board[i][j] = temp

        return found

    # Try starting from each cell
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True

    return False


def findAllWords(board, words):
    """
    Find all words from the list that exist in the board
    """
    result = []
    for word in words:
        if exist(board, word):
            result.append(word)
    return result


def wordSearchWithPath(board, word):
    """
    Return the path if word exists, otherwise return empty list
    """
    if not board or not board[0]:
        return []

    m, n = len(board), len(board[0])
    path = []

    def dfs(i, j, k):
        if k == len(word):
            return True

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = "#"
        path.append((i, j))

        if (
            dfs(i + 1, j, k + 1)
            or dfs(i - 1, j, k + 1)
            or dfs(i, j + 1, k + 1)
            or dfs(i, j - 1, k + 1)
        ):
            return True

        path.pop()
        board[i][j] = temp
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return path

    return []


# Test the function
if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    test_words = ["ABCCED", "SEE", "ABCB", "ASADEE", "ABFS"]

    print("Word Search")
    print("=" * 40)
    print("Board:")
    for row in board:
        print("  " + str(row))
    print()

    for word in test_words:
        result = exist(board, word)
        print(f"Word '{word}': {result}")

        if result:
            path = wordSearchWithPath(board, word)
            print(f"  Path: {path}")
        print()

    # Test with multiple words
    print("\nFinding all words from list:")
    words = ["ABCCED", "SEE", "ABCB", "ASF"]
    found = findAllWords(board, words)
    print(f"Words to find: {words}")
    print(f"Found: {found}")
