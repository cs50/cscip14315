from tictactoe import TicTacToe


def main():
    game = TicTacToe()
    while game.get_winner() is False:
        render_board(game.board)
        current_player = game.current_player
        move = input(f"{current_player}'s move (row, col): ")
        try:
            row, col = move.split(",")
            row = int(row.strip())
            col = int(col.strip())
            game.play_at(row, col)
        except ValueError:
            print("Illegal move.")
        print()

    render_board(game.board)
    winner = game.get_winner()
    if winner is None:
        print("It's a tie.")
    else:
        print(f"{winner} wins!")

def render_board(board):
    print_column_indices()
    print_horizontal_line()
    print_rows(board)

def print_column_indices():
    print("   ", end="")
    for i in range(3):
        print(f"  {i} ", end="")
    print()

def print_horizontal_line():
    print("   ", end="")
    print("-" * 13)

def print_rows(board):
    for i in range(3):
        print_row(board, i)

def print_row(board, row):
    print(f"{row}  |", end="")
    for col in range(3):
        print(f" {board[row][col]} |", end="")
    print()
    print_horizontal_line()

if __name__ == "__main__":
    main()