"""Generate Binary Strings using Branch and Bound."""

from __future__ import annotations


class BinaryStringNode:
    """Node representing a partial binary string in the search tree."""

    def __init__(self, string: str, level: int) -> None:
        self.string = string
        self.level = level


def _is_valid(string: str, constraint: str | None = None) -> bool:
    if constraint == "no_consecutive_ones":
        return "11" not in string
    return True


def generate_binary_strings(n: int, constraint: str | None = None) -> list[str]:
    """Generate all binary strings of length n using Branch and Bound.

    Args:
        n: Length of binary strings to generate.
        constraint: Optional constraint ('no_consecutive_ones' to avoid consecutive 1s).

    Returns:
        List of valid binary strings.
    """
    results: list[str] = []
    queue: list[BinaryStringNode] = [BinaryStringNode("", 0)]

    while queue:
        current = queue.pop(0)

        if current.level == n:
            results.append(current.string)
            continue

        for bit in ["0", "1"]:
            new_string = current.string + bit
            if _is_valid(new_string, constraint):
                child = BinaryStringNode(new_string, current.level + 1)
                queue.append(child)

    return results


def generate_binary_strings_recursive(
    n: int, constraint: str | None = None
) -> list[str]:
    """Generate all binary strings of length n using recursive Branch and Bound.

    Args:
        n: Length of binary strings to generate.
        constraint: Optional constraint ('no_consecutive_ones' to avoid consecutive 1s).

    Returns:
        List of valid binary strings.
    """
    results: list[str] = []

    def _backtrack(current: str, level: int) -> None:
        if not _is_valid(current, constraint):
            return

        if level == n:
            results.append(current)
            return

        _backtrack(current + "0", level + 1)
        _backtrack(current + "1", level + 1)

    _backtrack("", 0)
    return results


if __name__ == "__main__":
    n = 3

    print(f"All binary strings of length {n}:")
    results = generate_binary_strings(n)
    for s in results:
        print(s)

    print(f"\nBinary strings of length {n} without consecutive ones:")
    results_constrained = generate_binary_strings(n, constraint="no_consecutive_ones")
    for s in results_constrained:
        print(s)
