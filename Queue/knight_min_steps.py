from collections import deque


def isInside(x, y, n):
    return 1 <= x <= n and 1 <= y <= n


def minSteps(knightPos, targetPos, n):
    knight_x, knight_y = knightPos
    target_x, target_y = targetPos

    if [knight_x, knight_y] == [target_x, target_y]:
        return 0

    visited = set()
    queue = deque([(knight_x, knight_y, 0)])
    visited.add((knight_x, knight_y))

    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if new_x == target_x and new_y == target_y:
                return steps + 1

            if isInside(new_x, new_y, n) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))

    return -1


if __name__ == "__main__":
    n = 30
    knightPos = [1, 1]
    targetPos = [30, 30]
    print(f"Minimum steps: {minSteps(knightPos, targetPos, n)}")
