def knight_moves(position, board_size=8):
    """
    Find all possible moves of a knight from a given position on a chessboard.
    Position is given as (row, col) where 0 <= row, col < board_size.
    Returns a list of valid moves as (row, col) tuples.
    """
    # All possible knight moves relative to current position
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    row, col = position
    valid_moves = []

    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        # Check if the new position is within the board
        if 0 <= new_row < board_size and 0 <= new_col < board_size:
            valid_moves.append((new_row, new_col))

    return valid_moves


# Test cases
if __name__ == "__main__":
    # Test case 1: Knight at center of 8x8 board
    pos1 = (3, 3)
    moves1 = knight_moves(pos1)
    print(f"Knight at {pos1} can move to:")
    print(sorted(moves1))
    # Expected: 8 possible moves

    # Test case 2: Knight at corner of 8x8 board
    pos2 = (0, 0)
    moves2 = knight_moves(pos2)
    print(f"\nKnight at {pos2} can move to:")
    print(sorted(moves2))
    # Expected: [(1, 2), (2, 1)]

    # Test case 3: Knight near edge
    pos3 = (0, 3)
    moves3 = knight_moves(pos3)
    print(f"\nKnight at {pos3} can move to:")
    print(sorted(moves3))
    # Expected: [(1, 1), (1, 5), (2, 2), (2, 4)]

    # Test case 4: Custom board size
    pos4 = (0, 0)
    moves4 = knight_moves(pos4, board_size=5)
    print(f"\nKnight at {pos4} on 5x5 board can move to:")
    print(sorted(moves4))
    # Expected: [(1, 2), (2, 1)] (same as 8x8 since moves are within 5x5)
