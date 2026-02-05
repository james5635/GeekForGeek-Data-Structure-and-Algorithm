"""
Shortest Path to Print a String on Screen

Given a string, find the minimum time to print all characters on screen
where cursor can move in 4 directions (up, down, left, right) and
time to print a character is 1 unit.

This is based on the keyboard layout where characters are arranged.

Approach: Calculate Manhattan Distance - O(n) Time and O(1) Space
Calculate movement cost between consecutive characters on keyboard.
"""


def get_char_position(char):
    """
    Get position of character on QWERTY keyboard.
    Assuming keyboard layout:
    Row 0: qwertyuiop
    Row 1: asdfghjkl
    Row 2: zxcvbnm

    Args:
        char: Character to find

    Returns:
        (row, col) position
    """
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

    for row, keys in enumerate(keyboard):
        if char in keys:
            return (row, keys.index(char))

    return (0, 0)  # Default for unknown chars


def shortest_path_print(s):
    """
    Calculate minimum time to print string on screen.

    Args:
        s: Input string

    Returns:
        Total time units
    """
    total_time = 0
    current_pos = (0, 0)  # Start at 'q'

    for char in s.lower():
        if char.isalpha():
            target_pos = get_char_position(char)

            # Manhattan distance for movement
            movement_cost = abs(target_pos[0] - current_pos[0]) + abs(
                target_pos[1] - current_pos[1]
            )

            # 1 unit for printing
            total_time += movement_cost + 1
            current_pos = target_pos

    return total_time


def main():
    """Test cases for shortest path to print string."""
    test_cases = [
        ("abc", None),  # Depends on keyboard layout
        ("q", 1),
        ("qq", 2),
        ("qw", 3),  # Move 1 + print 1 + print 1
        ("az", None),
    ]

    print("=" * 50)
    print("Shortest Path to Print String")
    print("=" * 50)
    print("\nNote: Time includes movement + printing (1 unit each)")
    print("Keyboard layout assumed: QWERTY standard")
    print()

    for s, expected in test_cases:
        result = shortest_path_print(s)
        print(f"Input: '{s}'")
        print(f"Total time: {result} units")
        if expected:
            status = "✓" if result == expected else "✗"
            print(f"Expected: {expected} {status}")
        print()


if __name__ == "__main__":
    main()
