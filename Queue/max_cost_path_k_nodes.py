from collections import deque


def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def findShortestPath(n, edges, src, dst, k):
    graph = build_graph(n, edges)
    max_cost = -1

    queue = deque()
    queue.append((src, 0, 0))

    while queue:
        node, cost, intermediates = queue.popleft()

        if node == dst:
            max_cost = max(max_cost, cost)
            continue

        if intermediates > k:
            continue

        for neighbor, weight in graph[node]:
            if neighbor != src or intermediates == 0:
                queue.append((neighbor, cost + weight, intermediates + 1))

    return max_cost


if __name__ == "__main__":
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    result = findShortestPath(n, edges, src, dst, k)
    expected = 500
    print(f"Maximum cost path with at most {k} intermediate nodes: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}")
