#マスの管理


class Cell:
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def __init__(self):
        self.stone = Cell.EMPTY
        self.can_put = False

    @staticmethod
    def get_opponent(stone):
        if stone == Cell.BLACK:
            return Cell.WHITE
        return Cell.BLACK