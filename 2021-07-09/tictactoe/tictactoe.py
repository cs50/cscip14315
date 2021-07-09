class TicTacToe:
    def __init__(self):
        self.board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            self.board.append(row)

        self.current_player = "X"
        self.moves_left = 3 * 3

    def play_at(self, row, col):
        if row not in range(3) or col not in range(3) or \
            self.board[row][col] != " ":
            raise ValueError(f"Illegal move at ({row}, {col})")
        self.board[row][col] = self.current_player
        self.moves_left -= 1
        self.next_player()

    def next_player(self):
        winner = self.get_winner()
        if winner is False:
            self.current_player = "X" if self.current_player == "O" else "O"
        elif winner is None:
            self.current_player = None
        return self.current_player

    def get_winner(self):
        if self.diagonal_win() or self.horizontal_win() or self.vertical_win():
            return self.current_player
        if self.moves_left == 0:
            return None
        return False

    def diagonal_win(self):
        return self._top_left_to_bottom_right_win() or self._top_right_to_bottom_left_win()

    def _top_left_to_bottom_right_win(self):
        if self.board[0][0] != " ":
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
        return False

    def _top_right_to_bottom_left_win(self):
        if self.board[0][2] != " ":
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
        return False

    def horizontal_win(self):
        if self.board[0][0] != " ":
            if self.board[0][0] == self.board[0][1] == self.board[0][2]:
                return True

        if self.board[1][0] != " ":
            if self.board[1][0] == self.board[1][1] == self.board[1][2]:
                return True

        if self.board[2][0] != " ":
            if self.board[2][0] == self.board[2][1] == self.board[2][2]:
                return True

        return False

    def vertical_win(self):
        if self.board[0][0] != " ":
            if self.board[0][0] == self.board[1][0] == self.board[2][0]:
                return True

        if self.board[0][1] != " ":
            if self.board[0][1] == self.board[1][1] == self.board[2][1]:
                return True

        if self.board[0][2] != " ":
            if self.board[0][2] == self.board[1][2] == self.board[2][2]:
                return True

        return False