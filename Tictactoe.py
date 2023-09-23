
board = [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    return board[row][col] == " "


def check_winner(board, player):

    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def tic_tac_toe():
    player = "X"
    turns = 0

    while turns < 9:
        display_board(board)
        print(f"Ходит игрок {player}")

        row = int(input("Введите номер строки (0, 1, 2): "))
        col = int(input("Введите номер столбца (0, 1, 2): "))

        if is_valid_move(board, row, col):
            board[row][col] = player
            turns += 1

            if check_winner(board, player):
                display_board(board)
                print(f"Игрок {player} выиграл!")
                break
            elif turns == 9:
                display_board(board)
                print("Ничья!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("Неверный ход. Попробуйте снова.")

if __name__ == "__main__":
    tic_tac_toe()