import sys


def minimumCostSimplePath(V, graph, s, t):
    INF = sys.maxsize
    visited = [False] * V

    def dfs(node, cost):
        if node == t:
            return cost
        visited[node] = True
        min_cost = INF
        for neighbor in range(V):
            if not visited[neighbor] and graph[node][neighbor] != INF:
                result = dfs(neighbor, cost + graph[node][neighbor])
                if result < min_cost:
                    min_cost = result
        visited[node] = False
        return min_cost

    result = dfs(s, 0)
    return result if result != INF else -1


if __name__ == "__main__":
    INF = 10**9
    V = 3
    graph = [[INF, -2, INF], [INF, INF, -1], [INF, INF, INF]]

    s, t = 0, 2
    expected = -3

    print(f"Minimum Cost: {minimumCostSimplePath(V, graph, s, t)}")
    print(f"Expected: {expected}")
