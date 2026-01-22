"""Expected Approach - Using Branch and Bound - O(n^2 * n!) Time and O(n^2) Space"""


import heapq

# Define the dimensions of the puzzle
N = 3


# State space tree node
class Node:
    def __init__(
        self, mat: list[list[int]], x: int, y: int, level: int, parent: "Node | None"
    ):
        self.parent = parent
        self.mat = [row[:] for row in mat]  # Deep copy
        self.x = x
        self.y = y
        self.cost = float("inf")
        self.level = level

    def __lt__(self, other):
        """Comparison for priority queue based on cost + level."""
        return (self.cost + self.level) < (other.cost + other.level)


# Bottom, left, top, right movement
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]


def print_matrix(mat: list[list[int]]) -> None:
    """Print N x N matrix."""
    for row in mat:
        print(" ".join(map(str, row)))


def calculate_cost(initial: list[list[int]], final: list[list[int]]) -> int:
    """
    Calculate misplaced tiles (heuristic function).
    
    >>> calculate_cost([[1, 2, 3], [4, 5, 6], [7, 8, 0]], [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    0
    >>> calculate_cost([[1, 2, 3], [4, 0, 5], [6, 7, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    2
    """
    count = 0
    for i in range(N):
        for j in range(N):
            if initial[i][j] != 0 and initial[i][j] != final[i][j]:
                count += 1
    return count


def is_safe(x: int, y: int) -> bool:
    """
    Check if coordinates are valid.
    
    >>> is_safe(0, 0)
    True
    >>> is_safe(3, 0)
    False
    """
    return 0 <= x < N and 0 <= y < N


def print_path(root: "Node | None") -> None:
    """Print path from root node to destination node."""
    if root is None:
        return
    print_path(root.parent)
    print_matrix(root.mat)
    print()


def solve(initial: list[list[int]], x: int, y: int, final: list[list[int]]) -> None:
    """
    Solve the 8-puzzle using Branch and Bound.
    
    Given a 3×3 board with 8 tiles (each numbered from 1 to 8) and one empty
    space, the objective is to place the numbers to match the final configuration
    using the empty space. We can slide four adjacent tiles (left, right, above,
    and below) into the empty space.
    
    Limitations of DFS and BFS in the 8-Puzzle Problem:
    - DFS: Can get stuck in deep, unproductive paths, leading to excessive
      memory usage and slow performance.
    - BFS: Explores all nodes at the current depth level, making it inefficient
      as it does not prioritize promising paths.
    
    Optimizing with Branch and Bound (B&B):
    Branch and Bound enhances search efficiency by using a cost function to guide
    exploration.
    
    1. Intelligent Node Selection: Prioritizes nodes closer to the goal, unlike
       DFS (blind) or BFS (equal priority).
    2. Pruning: Eliminates unpromising paths to save time and memory.
    
    Approach:
    - Use a priority queue to store live nodes.
    - Initialize the cost function for the root node.
    - Expand the least-cost node first.
    - Stop when a goal state is reached or when the queue is empty.
    
    Types of Nodes in B&B:
    - Live Node: Generated but not yet explored.
    - E-node (Expanding Node): Currently being expanded.
    - Dead Node: No longer considered (either solution found or cost too high).
    
    Cost Function for 8-Puzzle:
    C(X) = g(X) + h(X)
    Where:
    - g(X) = Moves taken to reach the current state.
    - h(X) = Number of misplaced tiles.
    
    Only nodes with the lowest cost function value are expanded, ensuring an
    optimal path.
    
    Time complexity: O(n^2 * n!)
    Auxiliary Space: O(n^2)
    
    >>> import io
    >>> import sys
    >>> old_stdout = sys.stdout
    >>> sys.stdout = buffer = io.StringIO()
    >>> solve([[1, 0, 2], [3, 4, 5], [6, 7, 8]], 0, 1, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    >>> output = buffer.getvalue()
    >>> sys.stdout = old_stdout
    >>> len(output) > 0
    True
    """
    pq = []
    root = Node(initial, x, y, 0, None)
    root.cost = calculate_cost(initial, final)
    heapq.heappush(pq, root)

    while pq:
        min_node = heapq.heappop(pq)

        # If final state is reached, print the solution path
        if min_node.cost == 0:
            print_path(min_node)
            return

        # Generate all possible child nodes
        for i in range(4):
            new_x, new_y = min_node.x + row[i], min_node.y + col[i]
            if is_safe(new_x, new_y):
                new_mat = [row[:] for row in min_node.mat]
                # Swap blank tile
                new_mat[min_node.x][min_node.y], new_mat[new_x][new_y] = (
                    new_mat[new_x][new_y],
                    new_mat[min_node.x][min_node.y],
                )
                child = Node(new_mat, new_x, new_y, min_node.level + 1, min_node)
                child.cost = calculate_cost(child.mat, final)
                heapq.heappush(pq, child)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    # Example usage
    print("\nExample: 8-Puzzle using Branch and Bound")
    print("=" * 40)
    # Initial configuration
    initial = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

    # Solvable Final configuration
    final = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Blank tile coordinates in initial configuration
    x, y = 0, 1

    solve(initial, x, y, final)
