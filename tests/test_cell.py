
from models.cell import Cell

def test_cell_init():
    cell = Cell()

    assert cell.stone == Cell.EMPTY
    assert not cell.can_put


def test_get_opponent():
    assert Cell.get_opponent(Cell.BLACK) == Cell.WHITE
    assert Cell.get_opponent(Cell.WHITE) == Cell.BLACK