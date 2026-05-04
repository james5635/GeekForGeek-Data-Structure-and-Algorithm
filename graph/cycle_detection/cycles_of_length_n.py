"""
Count Cycles of Length n in an Undirected and Connected Graph

Problem: Given an undirected connected graph and a number n, count the total
number of simple cycles of length n. A simple cycle of length n contains exactly
n vertices and n edges.

Algorithm: DFS-based path enumeration
1. For each starting vertex, use DFS to find all paths of length (n-1)
2. Check if the path can be closed back to the starting vertex
3. Since undirected cycles are counted twice (once in each direction), divide by 2
4. Only need to check V - (n - 1) starting vertices because the remaining vertices
   are covered by paths from earlier starting points

Time Complexity: O(V^V) in worst case (exponential for large graphs)
Space Complexity: O(V) for the marked array and recursion stack
"""


def count_cycles_of_length_n(adj_matrix: list[list[int]], n: int) -> int:
    """
    Count the number of simple cycles of length n in an undirected connected graph.

    Args:
        adj_matrix: Adjacency matrix where adj_matrix[i][j] = 1 if edge exists
        n: The length of cycles to count

    Returns:
        Number of unique simple cycles of length n
    """
    V = len(adj_matrix)

    if n > V or n < 3:
        return 0

    def dfs(vert: int, start: int, length: int, marked: list[bool]) -> int:
        marked[vert] = True
        count = 0

        if length == 0:
            marked[vert] = False
            if adj_matrix[vert][start] == 1:
                return 1
            return 0

        for i in range(V):
            if not marked[i] and adj_matrix[vert][i] == 1:
                count += dfs(i, start, length - 1, marked)

        marked[vert] = False
        return count

    total_count = 0
    marked: list[bool] = [False] * V

    for i in range(V - (n - 1)):
        total_count += dfs(i, i, n - 1, marked)
        marked[i] = True

    return total_count // 2


def count_cycles_with_paths(
    adj_matrix: list[list[int]], n: int
) -> tuple[int, list[list[int]]]:
    """
    Count cycles of length n and return the actual cycle paths.

    Args:
        adj_matrix: Adjacency matrix where adj_matrix[i][j] = 1 if edge exists
        n: The length of cycles to count

    Returns:
        Tuple of (count, list_of_cycles) where each cycle is a list of vertices
    """
    V = len(adj_matrix)

    if n > V or n < 3:
        return 0, []

    def dfs(
        vert: int, start: int, length: int, marked: list[bool], path: list[int]
    ) -> list[list[int]]:
        marked[vert] = True
        path.append(vert)
        cycles: list[list[int]] = []

        if length == 0:
            marked[vert] = False
            if adj_matrix[vert][start] == 1:
                cycles.append(path[:])
            path.pop()
            return cycles

        for i in range(V):
            if not marked[i] and adj_matrix[vert][i] == 1:
                cycles.extend(dfs(i, start, length - 1, marked, path))

        marked[vert] = False
        path.pop()
        return cycles

    all_cycles: list[list[int]] = []
    marked: list[bool] = [False] * V

    for i in range(V - (n - 1)):
        all_cycles.extend(dfs(i, i, n - 1, marked, []))
        marked[i] = True

    seen: set[tuple[int, ...]] = set()
    unique_cycles: list[list[int]] = []

    for cycle in all_cycles:
        key = tuple(cycle)
        reversed_key = tuple(cycle[0:1] + cycle[1:][::-1])
        if key not in seen and reversed_key not in seen:
            seen.add(key)
            unique_cycles.append(cycle)

    return len(unique_cycles), unique_cycles


if __name__ == "__main__":
    print("=" * 60)
    print("Count Cycles of Length n in Undirected Graph")
    print("=" * 60)

    # Example 1: Graph from GeeksforGeeks
    #   0 -- 1 -- 2
    #   |    |    |
    #   3 -- 4 -- (implied connections)
    #
    #   Adjacency matrix:
    #   0: connected to 1, 3
    #   1: connected to 0, 2, 4
    #   2: connected to 1, 3
    #   3: connected to 0, 2, 4
    #   4: connected to 1, 3
    print("\nExample 1: Count cycles of length 4")
    graph1 = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
    ]
    n1 = 4
    count1, paths1 = count_cycles_with_paths(graph1, n1)
    print(f"  Vertices: {len(graph1)}")
    print(f"  Cycle length: {n1}")
    print(f"  Total cycles of length {n1}: {count1}")
    for i, path in enumerate(paths1):
        print(f"    Cycle {i + 1}: {' -> '.join(map(str, path))} -> {path[0]}")

    # Example 2: Triangle (3-cycle)
    #   0 -- 1
    #    \  /
    #     2
    print("\nExample 2: Count cycles of length 3 in a triangle")
    graph2 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    n2 = 3
    count2, paths2 = count_cycles_with_paths(graph2, n2)
    print(f"  Vertices: {len(graph2)}")
    print(f"  Cycle length: {n2}")
    print(f"  Total cycles of length {n2}: {count2}")
    for i, path in enumerate(paths2):
        print(f"    Cycle {i + 1}: {' -> '.join(map(str, path))} -> {path[0]}")

    # Example 3: Square (4-cycle)
    #   0 -- 1
    #   |    |
    #   3 -- 2
    print("\nExample 3: Count cycles of length 4 in a square")
    graph3 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    n3 = 4
    count3 = count_cycles_of_length_n(graph3, n3)
    print(f"  Vertices: {len(graph3)}")
    print(f"  Cycle length: {n3}")
    print(f"  Total cycles of length {n3}: {count3}")

    # Example 4: Complete graph K4
    # Every vertex connected to every other vertex
    print("\nExample 4: Count cycles of length 3 in K4 (complete graph)")
    graph4 = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
    ]
    n4 = 3
    count4, paths4 = count_cycles_with_paths(graph4, n4)
    print(f"  Vertices: {len(graph4)}")
    print(f"  Cycle length: {n4}")
    print(f"  Total cycles of length {n4}: {count4}")
    for i, path in enumerate(paths4):
        print(f"    Cycle {i + 1}: {' -> '.join(map(str, path))} -> {path[0]}")

    print("\n" + "=" * 60)
