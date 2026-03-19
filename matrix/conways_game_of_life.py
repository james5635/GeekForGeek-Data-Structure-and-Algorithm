def game_of_life(board):
    """
    Implement Conway's Game of Life.
    According to Wikipedia's article: "The Game of Life, also known simply as Life,
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    Rules:
    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Args:
        board: 2D list representing the game board (1 = live, 0 = dead)

    Returns:
        None (modifies board in-place)
    """
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    # Create a copy of the board to calculate next state
    copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

    # Directions for 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(rows):
        for col in range(cols):
            # Count live neighbors
            live_neighbors = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and copy_board[new_row][new_col] == 1
                ):
                    live_neighbors += 1

            # Apply rules
            if copy_board[row][col] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    board[row][col] = 0  # Dies
            else:  # Dead cell
                if live_neighbors == 3:
                    board[row][col] = 1  # Becomes alive


def print_board(board):
    """Helper function to print the board"""
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Simple oscillator (blinker)
    print("Test 1: Blinker oscillator")
    board1 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    print("Initial state:")
    print_board(board1)
    game_of_life(board1)
    print("After one generation:")
    print_board(board1)
    game_of_life(board1)
    print("After two generations (should return to initial):")
    print_board(board1)

    # Test case 2: Block (still life)
    print("Test 2: Block (should remain unchanged)")
    board2 = [[1, 1], [1, 1]]
    print("Initial state:")
    print_board(board2)
    game_of_life(board2)
    print("After one generation (should be same):")
    print_board(board2)

    # Test case 3: Glider
    print("Test 3: Glider")
    board3 = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    print("Initial state:")
    print_board(board3)
    game_of_life(board3)
    print("After one generation:")
    print_board(board3)
