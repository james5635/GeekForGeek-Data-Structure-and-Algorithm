"""Naive Approach - Using BFS - O(n!) Time and O(n!) Space"""


from collections import deque

# Define the dimensions of the puzzle
N = 3


# Class to represent the state of the puzzle
class PuzzleState:
    def __init__(self, board: list[list[int]], x: int, y: int, depth: int):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth


# Possible moves: Left, Right, Up, Down
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]


def is_goal_state(board: list[list[int]]) -> bool:
    """
    Check if the current state is the goal state.
    
    >>> is_goal_state([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    True
    >>> is_goal_state([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    False
    """
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal


def is_valid(x: int, y: int) -> bool:
    """
    Check if a move is valid.
    
    >>> is_valid(0, 0)
    True
    >>> is_valid(3, 0)
    False
    """
    return 0 <= x < N and 0 <= y < N


def print_board(board: list[list[int]]) -> None:
    """Print the puzzle board."""
    for row in board:
        print(" ".join(map(str, row)))
    print("--------")


def solve_puzzle_bfs(start: list[list[int]], x: int, y: int) -> None:
    """
    Solve the 8-puzzle problem using Breadth-First Search.
    
    Given a 3×3 board with 8 tiles (each numbered from 1 to 8) and one empty
    space, the objective is to place the numbers to match the final configuration
    using the empty space. We can slide four adjacent tiles (left, right, above,
    and below) into the empty space.
    
    We can perform a Breadth-first search on the state space tree. This always
    finds a goal state nearest to the root. But no matter what the initial state
    is, the algorithm attempts the same sequence of moves like DFS.
    
    Limitations:
    - Breadth-first search on the state-space tree.
    - Always finds the nearest goal state.
    - Same sequence of moves irrespective of initial state.
    
    Step by step approach:
    - Start from the root node.
    - Explore all neighboring nodes at the present depth.
    - Move to the next depth level and repeat the process.
    - If a goal state is reached, return the solution.
    
    Time complexity: O(n!)
    Auxiliary Space: O(n!)
    
    >>> import io
    >>> import sys
    >>> old_stdout = sys.stdout
    >>> sys.stdout = buffer = io.StringIO()
    >>> solve_puzzle_bfs([[1, 2, 3], [4, 0, 5], [6, 7, 8]], 1, 1)
    >>> output = buffer.getvalue()
    >>> sys.stdout = old_stdout
    >>> 'Depth: 0' in output
    True
    """
    q = deque()
    visited = set()

    # Enqueue initial state
    q.append(PuzzleState(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while q:
        curr = q.popleft()

        # Print the current board state
        print(f"Depth: {curr.depth}")
        print_board(curr.board)

        # Check if goal state is reached
        if is_goal_state(curr.board):
            print(f"Goal state reached at depth {curr.depth}")
            return

        # Explore all possible moves
        for i in range(4):
            new_x = curr.x + row[i]
            new_y = curr.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [row[:] for row in curr.board]
                new_board[curr.x][curr.y], new_board[new_x][new_y] = (
                    new_board[new_x][new_y],
                    new_board[curr.x][curr.y],
                )

                # If this state has not been visited before, push to queue
                if tuple(map(tuple, new_board)) not in visited:
                    visited.add(tuple(map(tuple, new_board)))
                    q.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1))

    print("No solution found (BFS Brute Force reached depth limit)")


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    # Example usage
    print("\nExample: 8-Puzzle using BFS")
    print("=" * 40)
    start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # Initial state
    x, y = 1, 1

    print("Initial State:")
    print_board(start)

    solve_puzzle_bfs(start, x, y)
