def printTemplate(board):
    print("\n   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   \n")

def check_winner(board):
    # 0 | 1 | 2
    # __|___|___
    # 3 | 4 | 5
    # __|___|___
    # 6 | 7 | 8

    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ': #checks whether all three positions in the winning combination are the same and not empty
            return board[combo[0]]  # Return the winner ('X' or 'O')
    
    if ' ' not in board:
        return 'Tie'  # Game is a tie
    
    return None

def minimax(board, depth, is_maximizing):
    # Minimax algorithm implementation
    result = check_winner(board)
    
    # Terminal states
    if result == 'X':  # AI wins
        return 1
    elif result == 'O':  # Human wins
        return -1
    elif result == 'Tie':
        return 0
    
    if is_maximizing:
        best_score = float('-inf')  # Initialize best score to negative infinity
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move(board):
    """AI makes move using minimax"""
    best_score = float('-inf')
    best_move = None
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move