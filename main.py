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

def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1-9!")

def play_game():
    # Initialize empty board
    board = [' '] * 9
    
    # Let player choose their symbol
    player_symbol = ''
    while player_symbol not in ['X', 'O']:
        player_symbol = input("Choose your symbol (X/O): ").upper()
    
    ai_symbol = 'O' if player_symbol == 'X' else 'X'
    
    print(f"\nYou are '{player_symbol}', AI is '{ai_symbol}'")
    print("Positions:")
    print(" 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("\n")
    
    # Determine who goes first (X always starts)
    if player_symbol == 'X':
        current_turn = 'player'
    else:
        current_turn = 'ai'
    
    # Game loop
    while True:
        printTemplate(board)
        
        # Check for game over
        result = check_winner(board)
        if result:
            if result == 'Tie':
                print("It's a tie!")
            else:
                print(f"{result} wins!")
            break
        
        # Player's turn
        if current_turn == 'player':
            print("Your turn!")
            move = get_player_move(board)
            board[move] = player_symbol
            current_turn = 'ai'
        # AI's turn
        else:
            print("AI's turn...")
            move = ai_move(board)
            board[move] = ai_symbol
            print(f"AI chooses position {move + 1}")
            current_turn = 'player'
    
    # Ask if player wants to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    print("TIC-TAC-TOE GAME WITH AI\n")
    play_game()