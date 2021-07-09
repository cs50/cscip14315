import tkinter as tk

from tkinter import font

from tictactoe import TicTacToe


def main():
    window = create_window()
    TicTacToeGrid(window)
    window.mainloop()

def create_window():
    window_height = 256
    window_width = 256

    window = tk.Tk()
    window.geometry(f"{window_width}x{window_height}")
    window.title("Tic-Tac-Toe")
    window.resizable(False, False)

    # Stretch 1x1 window grid
    tk.Grid.rowconfigure(window, 0, weight=1)
    tk.Grid.columnconfigure(window, 0, weight=1)
    return window

class TicTacToeGrid(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add frame to window at (0, 0)
        # Stretch frame in all directions
        self.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self.game = TicTacToe()

        self.buttons_board = []
        for row in range(3):
            buttons_row = []
            for col in range(3):
                button = self._create_button(row, col)
                buttons_row.append(button)
            self.buttons_board.append(buttons_row)

        self._stretch_rows_and_columns()

    def _create_button(self, row, col):
        font_size = 18
        button_height = 64
        button_width = 64

        button = tk.Button(
            self,
            width=button_height,
            height=button_width,
            text=" ",
            font=font.Font(size=font_size),
            disabledforeground="black",
            command=lambda row=row, col=col: self.play_at(row, col),
        )
        button.grid(row=row, column=col)
        return button

    def _stretch_rows_and_columns(self):
        self._stretch_rows()
        self._stretch_columns()

    def _stretch_rows(self):
        for row in range(3):
            tk.Grid.rowconfigure(self, row, weight=1)

    def _stretch_columns(self):
        for col in range(3):
            tk.Grid.columnconfigure(self, col, weight=1)

    def disable_all_buttons(self):
        for row in range(3):
            for col in range(3):
                self.disable_button(row, col)

    def render_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons_board[row][col]["text"] = self.game.board[row][col]

    def disable_button(self, row, col):
        self.buttons_board[row][col]["state"] = tk.DISABLED

    def play_at(self, row, col):
        self.disable_button(row, col)
        self.game.play_at(row, col)
        self.render_board()
        if self.game.get_winner() is not False:
            self.disable_all_buttons()

if __name__ == "__main__":
    main()
