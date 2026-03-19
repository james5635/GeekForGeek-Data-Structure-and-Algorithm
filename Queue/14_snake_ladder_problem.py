from collections import deque


def get_min_dice_throws_bfs(move):
    n = len(move)
    visited = [False] * n
    queue = deque()
    queue.append((0, 0))
    visited[0] = True

    while queue:
        cell, moves = queue.popleft()

        if cell == n - 1:
            return moves

        for dice in range(1, 7):
            next_cell = cell + dice
            if next_cell < n and not visited[next_cell]:
                visited[next_cell] = True
                if move[next_cell] == -1:
                    queue.append((next_cell, moves + 1))
                else:
                    queue.append((move[next_cell], moves + 1))

    return -1


def get_min_dice_throws_dfs(move):
    n = len(move)
    visited = [False] * n
    min_moves = [float("inf")]

    def dfs(cell, moves):
        if cell == n - 1:
            min_moves[0] = min(min_moves[0], moves)
            return

        if moves >= min_moves[0]:
            return

        for dice in range(1, 7):
            next_cell = cell + dice
            if next_cell < n and not visited[next_cell]:
                visited[next_cell] = True
                if move[next_cell] == -1:
                    dfs(next_cell, moves + 1)
                else:
                    dfs(move[next_cell], moves + 1)
                visited[next_cell] = False

    visited[0] = True
    dfs(0, 0)
    return min_moves[0] if min_moves[0] != float("inf") else -1


if __name__ == "__main__":
    move = [-1] * 30
    move[2] = 21
    move[4] = 7
    move[10] = 25
    move[19] = 28
    move[26] = 0
    move[20] = 8
    move[16] = 3
    move[18] = 6
    print(get_min_dice_throws_bfs(move))
    print(get_min_dice_throws_dfs(move))

    move2 = [-1] * 30
    move2[2] = 21
    move2[4] = 7
    print(get_min_dice_throws_bfs(move2))
    print(get_min_dice_throws_dfs(move2))

    move3 = [-1] * 30
    print(get_min_dice_throws_bfs(move3))
    print(get_min_dice_throws_dfs(move3))
