"""
Maximum Weight Node

Given a maze with N cells where each cell has at most one exit (unidirectional),
find the cell with the maximum weight.

The weight of a cell is the sum of the indices of all cells that point to it.
If multiple cells have the same maximum weight, return the one with the highest index.

Edge[i] contains the cell index reachable from cell i in one step.
Edge[i] = -1 means cell i has no exit.

Example:
    Input: N = 4, Edge = [2, 0, -1, 2]
    Edges: 0->2, 1->0, 2->(none), 3->2

    Weight of cell 0: 1 (cell 1 points to it)
    Weight of cell 1: 0 (no cell points to it)
    Weight of cell 2: 0 + 3 = 3 (cells 0 and 3 point to it)
    Weight of cell 3: 0 (no cell points to it)

    Output: 2 (cell with maximum weight = 3)

Time Complexity: O(N)
Space Complexity: O(N)
"""


def max_weight_cell(num_cells: int, edges: list[int]) -> int:
    """
    Find the cell with the maximum weight in a directed graph.

    The weight of a cell is the sum of indices of all cells pointing to it.
    If there is a tie, the cell with the highest index is returned.

    Args:
        num_cells: Total number of cells (indexed 0 to N-1).
        edges: Array where edges[i] is the destination cell from cell i,
               or -1 if cell i has no exit.

    Returns:
        The index of the cell with the maximum weight.
    """
    # Initialize weight array
    weights = [0] * num_cells

    # Accumulate weights: for each edge i -> edges[i], add i to the destination's weight
    for i in range(num_cells):
        dest = edges[i]
        if dest != -1:
            weights[dest] += i

    # Find the cell with maximum weight
    # In case of tie, the highest index wins (use >= and iterate forward)
    max_idx = 0
    max_val = weights[0]

    for i in range(1, num_cells):
        if weights[i] >= max_val:
            max_val = weights[i]
            max_idx = i

    return max_idx


def get_all_weights(num_cells: int, edges: list[int]) -> list[int]:
    """
    Compute the weight of every cell in the graph.

    Args:
        num_cells: Total number of cells.
        edges: Edge array where edges[i] is the destination from cell i.

    Returns:
        A list where the i-th element is the weight of cell i.
    """
    weights = [0] * num_cells
    for i in range(num_cells):
        dest = edges[i]
        if dest != -1:
            weights[dest] += i
    return weights


if __name__ == "__main__":
    # Example 1: GFG example
    #   Edges: 0->2, 1->0, 2->(none), 3->2
    print("Example 1:")
    print("N = 4, Edge = [2, 0, -1, 2]")

    n1 = 4
    edges1 = [2, 0, -1, 2]

    weights1 = get_all_weights(n1, edges1)
    print("Weights per cell:")
    for i, w in enumerate(weights1):
        print(f"  Cell {i}: weight = {w}")

    result1 = max_weight_cell(n1, edges1)
    print(f"Maximum weight cell: {result1}")
    print()

    # Example 2: Single node
    print("Example 2:")
    print("N = 1, Edge = [-1]")

    n2 = 1
    edges2 = [-1]
    result2 = max_weight_cell(n2, edges2)
    print(f"Maximum weight cell: {result2}")
    print()

    # Example 3: All pointing to same cell
    #   0->3, 1->3, 2->3
    print("Example 3:")
    print("N = 4, Edge = [3, 3, 3, -1]")

    n3 = 4
    edges3 = [3, 3, 3, -1]

    weights3 = get_all_weights(n3, edges3)
    print("Weights per cell:")
    for i, w in enumerate(weights3):
        print(f"  Cell {i}: weight = {w}")

    result3 = max_weight_cell(n3, edges3)
    print(f"Maximum weight cell: {result3}")
    print()

    # Example 4: Tie-breaking (highest index wins)
    #   0->1, 2->3
    #   Weight of 1 = 0, Weight of 3 = 2 -> cell 3 wins
    print("Example 4 (tie-breaking demonstration):")
    print("N = 4, Edge = [1, -1, 3, -1]")

    n4 = 4
    edges4 = [1, -1, 3, -1]

    weights4 = get_all_weights(n4, edges4)
    print("Weights per cell:")
    for i, w in enumerate(weights4):
        print(f"  Cell {i}: weight = {w}")

    result4 = max_weight_cell(n4, edges4)
    print(f"Maximum weight cell: {result4}")
