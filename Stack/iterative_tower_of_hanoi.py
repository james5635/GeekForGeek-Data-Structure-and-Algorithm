def iterative_tower_of_hanoi(n, source="A", auxiliary="B", destination="C"):
    total_moves = 2**n - 1
    rods = {source: list(range(n, 0, -1)), auxiliary: [], destination: []}

    if n % 2 == 0:
        auxiliary, destination = destination, auxiliary

    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            _move_top(rods, source, destination)
        elif move % 3 == 2:
            _move_top(rods, source, auxiliary)
        else:
            _move_top(rods, auxiliary, destination)

    return rods


def _move_top(rods, from_rod, to_rod):
    from_top = rods[from_rod][-1] if rods[from_rod] else float("inf")
    to_top = rods[to_rod][-1] if rods[to_rod] else float("inf")

    if from_top < to_top:
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        print(f"Move disk {disk} from {from_rod} to {to_rod}")
    else:
        disk = rods[to_rod].pop()
        rods[from_rod].append(disk)
        print(f"Move disk {disk} from {to_rod} to {from_rod}")


if __name__ == "__main__":
    print("Tower of Hanoi with 3 disks:")
    rods = iterative_tower_of_hanoi(3)
    print("Final state:", rods)

    print("\nTower of Hanoi with 4 disks:")
    rods = iterative_tower_of_hanoi(4)
    print("Final state:", rods)
