def check_winner(board):
    for line in [board, zip(*board), [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]]:
        for trio in line:
            if trio[0] == trio[1] == trio[2] != " ":
                return trio[0]
    return None

def minimax(board, is_max):
    winner = check_winner(board)
    if winner: return 1 if winner == "X" else -1
    if all(cell != " " for row in board for cell in row): return 0
    scores = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "X" if is_max else "O"
                scores.append(minimax(board, not is_max))
                board[r][c] = " "
    return max(scores) if is_max else min(scores)

def best_move(board):
    best_score, move = float('-inf'), None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "X"
                score = minimax(board, False)
                board[r][c] = " "
                if score > best_score:
                    best_score, move = score, (r, c)
    return move

# Example usage
board = [["X", "O", "X"], [" ", "X", " "], ["O", " ", " "]]
print(f"Best move for 'X': {best_move(board)}")
