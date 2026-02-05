"""
Tower of Hanoi using Recursion

The Tower of Hanoi is a classic mathematical puzzle involving three rods (A, B, C)
and n disks of different sizes. Initially, all disks are stacked on rod A in
decreasing order of diameter. Goal: Move the entire stack to rod C following rules:

Rules:
1. Move only one disk at a time
2. Only top disk can be moved from any rod
3. No larger disk may be placed on top of a smaller disk

Approach:
The recursive pattern:
1. Shift 'n-1' disks from 'A' to 'B', using C as auxiliary
2. Shift the last (largest) disk from 'A' to 'C'
3. Shift 'n-1' disks from 'B' to 'C', using A as auxiliary

Time Complexity: O(2^n) - Each disk has 2 possibilities
Auxiliary Space: O(n) - Function call stack space
"""


def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    """
    Recursive function to solve Tower of Hanoi puzzle.

    Args:
        n: Number of disks
        from_rod: Source rod (where disks are initially)
        to_rod: Destination rod (where disks need to go)
        aux_rod: Auxiliary rod (helper rod)

    Returns:
        int: Number of moves made
    """
    # Base case: no disk to move
    if n == 0:
        return 0

    moves = 0

    # Move n-1 disks from from_rod to aux_rod, using to_rod
    moves += tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)

    # Move the nth disk from from_rod to to_rod
    print(f"Disk {n} moved from {from_rod} to {to_rod}")
    moves += 1

    # Move n-1 disks from aux_rod to to_rod, using from_rod
    moves += tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

    return moves


def tower_of_hanoi_with_steps(n, from_rod, to_rod, aux_rod, steps=None):
    """
    Version that collects steps in a list instead of printing.

    Args:
        n: Number of disks
        from_rod: Source rod
        to_rod: Destination rod
        aux_rod: Auxiliary rod
        steps: List to collect steps (optional)

    Returns:
        list: List of moves
    """
    if steps is None:
        steps = []

    if n == 0:
        return steps

    # Move n-1 disks from from_rod to aux_rod
    tower_of_hanoi_with_steps(n - 1, from_rod, aux_rod, to_rod, steps)

    # Move the nth disk
    step = f"Disk {n} moved from {from_rod} to {to_rod}"
    steps.append(step)

    # Move n-1 disks from aux_rod to to_rod
    tower_of_hanoi_with_steps(n - 1, aux_rod, to_rod, from_rod, steps)

    return steps


def main():
    # Test Case 1: 3 disks
    print("=" * 50)
    print("Tower of Hanoi with 3 disks")
    print("=" * 50)
    n1 = 3
    print(f"Number of disks: {n1}")
    print(f"Source rod: A, Destination rod: C, Auxiliary rod: B")
    print("-" * 50)
    total_moves1 = tower_of_hanoi(n1, "A", "C", "B")
    print("-" * 50)
    print(f"Total moves: {total_moves1}")
    print(f"Expected moves: {2**n1 - 1}")
    print()

    # Test Case 2: 2 disks
    print("=" * 50)
    print("Tower of Hanoi with 2 disks")
    print("=" * 50)
    n2 = 2
    print(f"Number of disks: {n2}")
    print(f"Source rod: A, Destination rod: C, Auxiliary rod: B")
    print("-" * 50)
    total_moves2 = tower_of_hanoi(n2, "A", "C", "B")
    print("-" * 50)
    print(f"Total moves: {total_moves2}")
    print(f"Expected moves: {2**n2 - 1}")
    print()

    # Test Case 3: 1 disk
    print("=" * 50)
    print("Tower of Hanoi with 1 disk")
    print("=" * 50)
    n3 = 1
    print(f"Number of disks: {n3}")
    print(f"Source rod: A, Destination rod: C, Auxiliary rod: B")
    print("-" * 50)
    total_moves3 = tower_of_hanoi(n3, "A", "C", "B")
    print("-" * 50)
    print(f"Total moves: {total_moves3}")
    print(f"Expected moves: {2**n3 - 1}")
    print()

    # Test Case 4: 4 disks (collecting steps)
    print("=" * 50)
    print("Tower of Hanoi with 4 disks (steps collected)")
    print("=" * 50)
    n4 = 4
    print(f"Number of disks: {n4}")
    steps = tower_of_hanoi_with_steps(n4, "A", "C", "B")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")
    print(f"Total moves: {len(steps)}")
    print(f"Expected moves: {2**n4 - 1}")


if __name__ == "__main__":
    main()
