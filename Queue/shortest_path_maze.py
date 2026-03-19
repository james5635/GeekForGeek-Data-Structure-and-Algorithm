from collections import deque


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def shortest_path_dfs(mat, src, dest):
    rows = len(mat)
    cols = len(mat[0])

    if mat[src.x][src.y] == 0 or mat[dest.x][dest.y] == 0:
        return -1

    visited = [[False] * cols for _ in range(rows)]

    def dfs(x, y, dist):
        if x == dest.x and y == dest.y:
            return dist

        visited[x][y] = True
        min_dist = float("inf")

        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in directions:
            if (
                is_valid(nx, ny, rows, cols)
                and mat[nx][ny] == 1
                and not visited[nx][ny]
            ):
                min_dist = min(min_dist, dfs(nx, ny, dist + 1))

        visited[x][y] = False
        return min_dist

    result = dfs(src.x, src.y, 0)
    return result if result != float("inf") else -1


def shortest_path_bfs(mat, src, dest):
    rows = len(mat)
    cols = len(mat[0])

    if mat[src.x][src.y] == 0 or mat[dest.x][dest.y] == 0:
        return -1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * cols for _ in range(rows)]
    queue = deque()

    queue.append(Point(src.x, src.y))
    visited[src.x][src.y] = True
    dist = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()

            if curr.x == dest.x and curr.y == dest.y:
                return dist

            for i in range(4):
                nx = curr.x + dx[i]
                ny = curr.y + dy[i]

                if (
                    is_valid(nx, ny, rows, cols)
                    and mat[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    queue.append(Point(nx, ny))

        dist += 1

    return -1


def shortestPath(mat, src, dest):
    return shortest_path_bfs(mat, src, dest)


if __name__ == "__main__":
    mat = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    ]

    src = Point(0, 0)
    dest = Point(3, 4)

    print("DFS Approach:", shortest_path_dfs(mat, src, dest))
    print("BFS Approach:", shortest_path_bfs(mat, src, dest))
    print("shortestPath function:", shortestPath(mat, src, dest))
    print("Expected: 11")
