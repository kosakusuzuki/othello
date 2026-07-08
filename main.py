from models.cell import Cell
from models.board import Board

board = Board()
turn = Cell.BLACK

while True:
    board.update_can_put(turn)
    board.print_board()

    if not board.has_valid_move(turn):
        opponent = Cell.get_opponent(turn)
        if not board .has_valid_move(opponent):
            print("ゲーム終了")
            break
        print("置ける場所がありません")
        turn = Cell.get_opponent(turn)
        continue

    row = int(input("行を入力："))
    col = int(input("列を入力："))

    if board.put_stone(row, col, turn):
        turn = Cell.get_opponent(turn)
    else:
        print("そのマスには置けません")
black, white = board.count_stones()

print(f"黒：{black}")
print(f"白：{white}")

if black > white:
    print("黒の勝ち")
elif white > black:
    print("白の勝ち")
else:
    print("引き分け")