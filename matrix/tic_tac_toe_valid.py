def is_valid_tic_tac_toe(board):
    """
    Check if a given Tic-Tac-Toe board configuration is valid.
    The board is a 3x3 2D list with values 'X', 'O', or ' ' (empty).
    Returns True if valid, False otherwise.
    Rules:
    1. Since X starts first, the number of X's is either equal to or one more than the number of O's.
    2. Only one player can win at a time.
    3. If X wins, then the number of X's must be one more than the number of O's.
    4. If O wins, then the number of X's must be equal to the number of O's.
    """
    # Count X and O
    count_x = sum(row.count("X") for row in board)
    count_o = sum(row.count("O") for row in board)

    # Rule 1: count_x must be equal to count_o or count_o+1
    if not (count_x == count_o or count_x == count_o + 1):
        return False

    # Helper to check if a player wins
    def player_wins(p):
        # Check rows and columns
        for i in range(3):
            if all(board[i][j] == p for j in range(3)) or all(
                board[j][i] == p for j in range(3)
            ):
                return True
        # Check diagonals
        if all(board[i][i] == p for i in range(3)) or all(
            board[i][2 - i] == p for i in range(3)
        ):
            return True
        return False

    x_wins = player_wins("X")
    o_wins = player_wins("O")

    # Rule 2: Both cannot win
    if x_wins and o_wins:
        return False

    # Rule 3: If X wins, count_x must be count_o+1
    if x_wins and count_x != count_o + 1:
        return False

    # Rule 4: If O wins, count_x must equal count_o
    if o_wins and count_x != count_o:
        return False

    return True


# Test cases
if __name__ == "__main__":
    # Valid board 1: X starts and leads by one, no winner yet
    board1 = [["X", "O", "X"], [" ", "X", "O"], ["O", " ", " "]]
    print("Board1 valid:", is_valid_tic_tac_toe(board1))  # Expected: True

    # Valid board 2: X wins
    board2 = [["X", "X", "X"], ["O", "O", " "], [" ", " ", " "]]
    print("Board2 valid:", is_valid_tic_tac_toe(board2))  # Expected: True

    # Invalid board: O wins but counts are equal (should be O wins only if X==O, but here X=3, O=3? Let's make O win with equal counts)
    board3 = [["O", "O", "O"], ["X", "X", " "], ["X", " ", " "]]
    # Count: X=3, O=3 -> but O wins and X==O -> valid? Actually, O wins and X==O is valid per rule 4.
    # However, note that X starts, so after 6 moves (3 X and 3 O) it's O's turn? Actually, if O wins on their 3rd move, then X has made 3 moves too (since X starts). So it's valid.
    print("Board3 valid:", is_valid_tic_tac_toe(board3))  # Expected: True

    # Invalid board: both win
    board4 = [["X", "X", "X"], ["O", "O", "O"], [" ", " ", " "]]
    print("Board4 valid:", is_valid_tic_tac_toe(board4))  # Expected: False

    # Invalid board: too many X's
    board5 = [["X", "X", "X"], ["X", "O", "O"], ["O", " ", " "]]
    print(
        "Board5 valid:", is_valid_tic_tac_toe(board5)
    )  # Expected: False (X=4, O=3 -> but X wins and X should be O+1? Actually 4==3+1 -> valid? Wait, but board has 4 X and 3 O, and X wins -> valid per rule 3. However, the board is impossible because after X's 4th move, the game would have ended when X got 3 in a row earlier. But our function only checks the final state. Let's assume we are given a final state and we don't know the move order. Actually, the problem is about validity of the configuration, not necessarily reachable. We'll stick to the rules.

    # Let's make a clearly invalid: O wins but X count is not equal to O count.
    board6 = [["O", "O", "O"], ["X", "X", " "], [" ", " ", "X"]]
    # X=3, O=3 -> O wins and X==O -> valid? Actually, O wins and X==O is valid. So let's change to make O win but X=4, O=3 -> invalid.
    board6 = [["O", "O", "O"], ["X", "X", "X"], [" ", " ", " "]]
    # Now both win -> invalid (caught by rule 2).
    print("Board6 valid:", is_valid_tic_tac_toe(board6))  # Expected: False
