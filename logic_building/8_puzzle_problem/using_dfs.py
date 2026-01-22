"""Naive Approach - Using DFS - O(n!) Time and O(n!) Space"""


# Define the dimensions of the puzzle
N = 3


# Structure to store a state of the puzzle
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
    Check if a given state is the goal state.
    
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
    >>> is_valid(-1, 0)
    False
    """
    return 0 <= x < N and 0 <= y < N


def print_board(board: list[list[int]]) -> None:
    """Print the board."""
    for row in board:
        print(" ".join(map(str, row)))
    print("--------")


def solve_puzzle_dfs(start: list[list[int]], x: int, y: int) -> None:
    """
    Solve the 8-puzzle problem using Depth-First Search.
    
    Given a 3×3 board with 8 tiles (each numbered from 1 to 8) and one empty
    space, the objective is to place the numbers to match the final configuration
    using the empty space. We can slide four adjacent tiles (left, right, above,
    and below) into the empty space.
    
    We can perform a depth-first search on state-space (Set of all configurations
    of a given problem i.e. all states that can be reached from the initial state)
    tree.
    
    Limitations:
    - Depth-first search on state-space tree.
    - Successive moves may take us away from the goal.
    - Inefficient as it explores all paths equally.
    
    Step by step approach:
    - Start from the root node.
    - Explore the leftmost child node recursively until you reach a leaf node or
      a goal state.
    - If a goal state is reached, return the solution.
    - If a leaf node is reached without finding a solution, backtrack to explore
      other branches.
    
    Time complexity: O(n!)
    Auxiliary Space: O(n!)
    
    >>> import io
    >>> import sys
    >>> old_stdout = sys.stdout
    >>> sys.stdout = buffer = io.StringIO()
    >>> solve_puzzle_dfs([[1, 2, 3], [4, 0, 5], [6, 7, 8]], 1, 1)
    >>> output = buffer.getvalue()
    >>> sys.stdout = old_stdout
    >>> 'Depth: 0' in output
    True
    """
    stack = []
    visited = set()

    stack.append(PuzzleState(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while stack:
        curr = stack.pop()

        # Print the current board
        print(f"Depth: {curr.depth}")
        print_board(curr.board)

        # Check if goal state is reached
        if is_goal_state(curr.board):
            print(f"Goal state reached at depth {curr.depth}")
            return

        # Explore possible moves
        for i in range(4):
            new_x = curr.x + row[i]
            new_y = curr.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [row[:] for row in curr.board]
                # Swap the tiles
                new_board[curr.x][curr.y], new_board[new_x][new_y] = (
                    new_board[new_x][new_y],
                    new_board[curr.x][curr.y],
                )

                # If this state has not been visited before, push to stack
                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1))

    print("No solution found (DFS Brute Force reached depth limit)")


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    # Example usage
    print("\nExample: 8-Puzzle using DFS")
    print("=" * 40)
    start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    x, y = 1, 1

    print("Initial State:")
    print_board(start)

    solve_puzzle_dfs(start, x, y)
