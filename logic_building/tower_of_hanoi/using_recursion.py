"""Approach: Tower of Hanoi using Recursion"""


def tower_of_hanoi(n: int, from_rod: str, to_rod: str, aux_rod: str) -> None:
    """
    Solve the Tower of Hanoi puzzle using recursion.
    
    The Tower of Hanoi is a classic mathematical puzzle involving three rods
    (A, B, and C) and n disks of different sizes. Initially, all disks are
    stacked on rod A in decreasing order of diameter - the largest disk at the
    bottom and the smallest at the top.
    
    Goal is to move the entire stack to another rod (rod C) while following
    these rules:
    - Move only one disk at a time.
    - At each step, you can take the top disk from any rod and place it on
      another rod.
    - A disk can only be moved if it is the topmost disk of a rod.
    - No larger disk may be placed on top of a smaller disk.
    
    The idea is to use the helper node to reach the destination using recursion.
    Below is the pattern for this problem:
    - Shift 'n-1' disks from 'A' to 'B', using C.
    - Shift last disk from 'A' to 'C'.
    - Shift 'n-1' disks from 'B' to 'C', using A.
    
    Follow the steps below to solve the problem:
    - Create a function towerOfHanoi where pass the n (current number of disk),
      fromRod, toRod, auxRod.
    - Make a function call for n - 1 th disk.
    - Then print the current the disk along with from_rod and to_rod
    - Again make a function call for n - 1 th disk.
    
    Time complexity: O(2^n). There are two possibilities for every disk.
    Therefore, 2 * 2 * 2 * ... * 2(n times) is 2^n.
    
    Auxiliary Space: O(n), Function call stack space.
    
    >>> import io
    >>> import sys
    >>> old_stdout = sys.stdout
    >>> sys.stdout = buffer = io.StringIO()
    >>> tower_of_hanoi(2, 'A', 'C', 'B')
    >>> output = buffer.getvalue()
    >>> sys.stdout = old_stdout
    >>> 'Disk 1 moved from A to B' in output
    True
    >>> 'Disk 2 moved from A to C' in output
    True
    >>> 'Disk 1 moved from B to C' in output
    True
    """
    if n == 0:
        return
    
    # Move n-1 disks from from_rod to aux_rod using to_rod as auxiliary
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    
    # Move the nth disk from from_rod to to_rod
    print(f"Disk {n} moved from {from_rod} to {to_rod}")
    
    # Move n-1 disks from aux_rod to to_rod using from_rod as auxiliary
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
    
    # Example usage
    print("\nExample: Tower of Hanoi with 3 disks")
    print("=" * 40)
    tower_of_hanoi(3, 'A', 'C', 'B')
