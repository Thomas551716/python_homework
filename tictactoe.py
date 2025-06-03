# tictactoe.py
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" "]*3 for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = [
            f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n",
            "-----------\n",
            f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n",
            "-----------\n",
            f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n"
        ]
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row, column = divmod(move_index, 3)
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        cat = all(cell != " " for row in self.board_array for cell in row)
        win = False
        for i in range(3):
            if self.board_array[i][0] != " " and len(set(self.board_array[i])) == 1:
                win = True
        for i in range(3):
            if self.board_array[0][i] != " " and \
               self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                win = True
        if self.board_array[1][1] != " ":
            if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                win = True
            if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                win = True
        if win:
            return (True, f"{'O' if self.turn == 'X' else 'X'} wins!")
        elif cat:
            return (True, "Cat's Game.")
        else:
            return (False, f"{self.turn}'s turn.")

if __name__ == "__main__":
    board = Board()
    while True:
        print(board)
        move = input(f"{board.turn}'s move: ").lower()
        try:
            board.move(move)
        except TictactoeException as e:
            print(f"Error: {e.message}")
            continue
        game_over, message = board.whats_next()
        if game_over:
            print(board)
            print(message)
            break

