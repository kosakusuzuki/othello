from board import Board
from models.cell import Cell

def test_can_put():
    board = Board()

    assert board.can_put(2,3,Cell.BLACK)

def test_can_put_black():
    board = Board()

    assert board.can_put(2,3,Cell.BLACK)
    assert board.can_put(3,2,Cell.BLACK)
    assert board.can_put(4,5,Cell.BLACK)
    assert board.can_put(5,4,Cell.BLACK)

def test_is_inside():
    board = Board()
    assert board.is_inside(7, 7)
    assert not board.is_inside(0, 8)

def test_get_stone():
    board = Board()
    assert board.get_stone(3, 3) == Cell.WHITE
    assert board.get_stone(3, 4) == Cell.BLACK
    assert board.get_stone(0, 0) == Cell.EMPTY

def test_get_next_stone():
    board = Board()

    assert board.get_next_stone(3, 3, 0, 1) == Cell.BLACK
    assert board.get_next_stone(3, 4, 0, -1) == Cell.WHITE
    assert board.get_next_stone(3, 3, 1, 0) == Cell.BLACK


def test_has_opponent_in_direction():
    board = Board()

    assert board.has_opponent_in_direction(2, 3, 1, 0, Cell.BLACK)
    assert not board.has_opponent_in_direction(2, 3, 0, -1, Cell.BLACK)

def test_update_can_put():
    board = Board()

    board.update_can_put(Cell.BLACK)

    assert board.cells[2][3].can_put
    assert board.cells[3][2].can_put
    assert board.cells[4][5].can_put
    assert board.cells[5][4].can_put

def test_flip_in_direction():
    board = Board()

    board.flip_in_direction(2,3,1,0, Cell.BLACK)
    assert board.get_stone(3, 3) == Cell.BLACK

def test_has_valid_move():
    board = Board()

    assert board.has_valid_move(Cell.BLACK)
    assert board.has_valid_move(Cell.WHITE)

def test_count_stones():
    board = Board()
    assert board.count_stones() == (2, 2)
    

