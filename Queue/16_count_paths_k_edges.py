def count_paths_recursive(graph, src, dest, k):
    n = len(graph)

    def dfs(u, remaining):
        if remaining == 0:
            return 1 if u == dest else 0
        count = 0
        for v in range(n):
            if graph[u][v]:
                count += dfs(v, remaining - 1)
        return count

    return dfs(src, k)


def count_paths_dp(graph, src, dest, k):
    n = len(graph)
    dp = [[0] * (k + 1) for _ in range(n)]

    dp[src][0] = 1

    for length in range(1, k + 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v]:
                    dp[v][length] += dp[u][length - 1]

    return dp[dest][k]


if __name__ == "__main__":
    graph1 = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    print(count_paths_recursive(graph1, 0, 3, 2))
    print(count_paths_dp(graph1, 0, 3, 2))

    graph2 = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    print(count_paths_recursive(graph2, 0, 4, 4))
    print(count_paths_dp(graph2, 0, 4, 4))

    graph3 = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    print(count_paths_recursive(graph3, 0, 2, 1))
    print(count_paths_dp(graph3, 0, 2, 1))
