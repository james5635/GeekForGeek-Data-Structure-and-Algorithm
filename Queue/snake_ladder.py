from collections import deque


def getMinDiceThrows(moves):
    return getMinDiceThrowsBFS(moves)


def getMinDiceThrowsBFS(moves):
    n = len(moves)
    visited = [False] * n
    queue = deque()
    queue.append((0, 0))
    visited[0] = True

    while queue:
        cell, throws = queue.popleft()

        if cell == n - 1:
            return throws

        for dice in range(1, 7):
            next_cell = cell + dice
            if next_cell < n and not visited[next_cell]:
                visited[next_cell] = True
                if moves[next_cell] == -1:
                    queue.append((next_cell, throws + 1))
                else:
                    queue.append((moves[next_cell], throws + 1))

    return -1


def getMinDiceThrowsDFS(moves):
    n = len(moves)
    visited = [False] * n
    min_moves = [float("inf")]

    def dfs(cell, throws):
        if cell == n - 1:
            min_moves[0] = min(min_moves[0], throws)
            return

        if throws >= min_moves[0]:
            return

        for dice in range(1, 7):
            next_cell = cell + dice
            if next_cell < n and not visited[next_cell]:
                visited[next_cell] = True
                if moves[next_cell] == -1:
                    dfs(next_cell, throws + 1)
                else:
                    dfs(moves[next_cell], throws + 1)
                visited[next_cell] = False

    visited[0] = True
    dfs(0, 0)
    return min_moves[0] if min_moves[0] != float("inf") else -1


if __name__ == "__main__":
    moves = [-1] * 30

    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    expected = 3

    bfs_result = getMinDiceThrowsBFS(moves)
    dfs_result = getMinDiceThrowsDFS(moves)

    print(
        f"BFS Result: {bfs_result}, Expected: {expected}, Test passed: {bfs_result == expected}"
    )
    print(
        f"DFS Result: {dfs_result}, Expected: {expected}, Test passed: {dfs_result == expected}"
    )
